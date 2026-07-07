from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse, JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.database.session import get_db
from app.models.scan import Scan
from app.services.report_service import ReportService
import os

router = APIRouter()

async def fetch_scan(scan_id: int, db: AsyncSession) -> Scan:
    result = await db.execute(
        select(Scan)
        .options(selectinload(Scan.threat_results), selectinload(Scan.recommendations), selectinload(Scan.official_websites))
        .filter(Scan.id == scan_id)
    )
    scan = result.scalars().first()
    if not scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    return scan

@router.get("/api/report/{scan_id}")
async def get_report(scan_id: int, db: AsyncSession = Depends(get_db)):
    scan = await fetch_scan(scan_id, db)
    return ReportService.generate_json(scan)

@router.get("/api/report/{scan_id}/json")
async def get_report_json(scan_id: int, db: AsyncSession = Depends(get_db)):
    scan = await fetch_scan(scan_id, db)
    return JSONResponse(content=ReportService.generate_json(scan))

@router.get("/api/report/{scan_id}/markdown")
async def get_report_markdown(scan_id: int, db: AsyncSession = Depends(get_db)):
    scan = await fetch_scan(scan_id, db)
    md_content = ReportService.generate_markdown(scan)
    return PlainTextResponse(content=md_content)

@router.get("/api/report/{scan_id}/download")
async def download_report_pdf(scan_id: int, db: AsyncSession = Depends(get_db)):
    scan = await fetch_scan(scan_id, db)
    pdf_path = ReportService.generate_pdf(scan)
    return FileResponse(
        path=pdf_path,
        filename=f"TrustGuardAI_Report_{scan_id}.pdf",
        media_type="application/pdf"
    )

@router.get("/api/report/history")
async def get_report_history(db: AsyncSession = Depends(get_db)):
    # In real app, filter by current_user.id
    result = await db.execute(select(Scan).order_by(Scan.created_at.desc()).limit(20))
    scans = result.scalars().all()
    return [{"id": s.id, "target": s.target, "risk_level": s.risk_level, "date": str(s.created_at)} for s in scans]
