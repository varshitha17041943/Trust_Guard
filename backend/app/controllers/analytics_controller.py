from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func, desc, Date, cast
from app.database.session import get_db
from app.models.scan import Scan
import time

router = APIRouter()

class DashboardCache:
    def __init__(self, ttl=60):
        self.ttl = ttl
        self.data = None
        self.last_updated = 0
        
    def get(self):
        if self.data and time.time() - self.last_updated < self.ttl:
            return self.data
        return None
        
    def set(self, data):
        self.data = data
        self.last_updated = time.time()

cache = DashboardCache()

@router.get("/api/analytics/dashboard")
async def get_dashboard(db: AsyncSession = Depends(get_db)):
    cached = cache.get()
    if cached:
        return cached
        
    # 1. Basic Stats
    total_scans_result = await db.execute(select(func.count(Scan.id)))
    total_scans = total_scans_result.scalar() or 0
    
    avg_risk_result = await db.execute(select(func.avg(Scan.risk_score)))
    avg_risk = float(avg_risk_result.scalar() or 0.0)
    
    # 2. Risk Distribution
    levels = await db.execute(select(Scan.risk_level, func.count(Scan.id)).group_by(Scan.risk_level))
    distribution = {row[0]: row[1] for row in levels.all()}
    
    # 3. Daily Trend
    trend_query = await db.execute(
        select(
            func.date(Scan.created_at).label('d'), 
            func.count(Scan.id)
        ).group_by('d').order_by('d').limit(7)
    )
    daily_trend = [{"name": str(row[0]), "scans": row[1]} for row in trend_query.all()]
    
    # 4. Threat Categories (Using threat intel results)
    # For now, derive from Risk Distribution to keep the pie chart dynamic but stable based on DB
    threat_categories = [
        {"name": "Critical", "value": distribution.get("Critical", 0)},
        {"name": "High", "value": distribution.get("High", 0)},
        {"name": "Low", "value": distribution.get("Low", 0)},
    ]
    # Filter out empty
    threat_categories = [c for c in threat_categories if c["value"] > 0]
    
    data = {
        "total_scans": total_scans,
        "average_risk": round(avg_risk, 1),
        "risk_distribution": distribution,
        "daily_trend": daily_trend,
        "threat_categories": threat_categories
    }
    
    cache.set(data)
    return data

@router.get("/api/analytics/history")
async def get_history(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Scan).order_by(desc(Scan.created_at)).limit(50))
    scans = result.scalars().all()
    return [
        {
            "id": s.id,
            "target": s.target,
            "scan_type": s.scan_type,
            "risk_level": s.risk_level,
            "risk_score": s.risk_score,
            "date": str(s.created_at)
        } for s in scans
    ]
