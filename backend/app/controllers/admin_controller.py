from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app.database.session import get_db
from app.models.scan import Scan

router = APIRouter()

@router.get("/api/admin/stats")
async def get_admin_stats(db: AsyncSession = Depends(get_db)):
    # Role-Based Access Control (RBAC) would be checked here via JWT Dependency
    scans_res = await db.execute(select(func.count(Scan.id)))
    blocked_res = await db.execute(select(func.count(Scan.id)).where(Scan.risk_level == "Critical"))
    
    return {
        "total_users": 142, # Mock
        "total_scans": scans_res.scalar() or 0,
        "blocked_urls": blocked_res.scalar() or 0,
        "active_threats": 12
    }
