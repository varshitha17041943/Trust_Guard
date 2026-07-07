from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.schemas.scan import URLScanRequest, QRScanRequest
from app.workflows.engine import stream_workflow
from app.models.scan import Scan
from app.models.details import ThreatResult, Recommendation, OfficialWebsite
import json

router = APIRouter()

async def save_state_to_db(db: AsyncSession, state_dict: dict, user_id: int | None = None) -> int:
    scan = Scan(
        target=state_dict.get("original_target"),
        scan_type=state_dict.get("scan_type"),
        status="completed",
        risk_score=state_dict.get("risk_score"),
        risk_level=state_dict.get("risk_level"),
        confidence_score=state_dict.get("confidence"),
        user_id=user_id
    )
    db.add(scan)
    await db.flush()
    
    for flag in state_dict.get("threat_intel_flags", []):
        db.add(ThreatResult(scan_id=scan.id, agent_name="ThreatIntelAgent", status="Fail", description=flag, passed=False))
        
    for rec in state_dict.get("recommendations", []):
        db.add(Recommendation(scan_id=scan.id, text=rec, priority="High"))
        
    impersonated = state_dict.get("impersonated_brand")
    if impersonated:
        db.add(OfficialWebsite(scan_id=scan.id, brand_name=impersonated, official_url=state_dict.get("official_url", "")))
        
    await db.commit()
    return scan.id

async def event_generator(db: AsyncSession, target: str, scan_type: str, user_id: int | None = None):
    final_state = None
    async for event in stream_workflow(target, scan_type):
        # Check if it's the final payload
        if "workflow_complete" in event:
            data_str = event.split("data: ")[1].strip()
            parsed = json.loads(data_str)
            final_state = parsed.get("state")
        else:
            yield event
            
    if final_state:
        scan_id = await save_state_to_db(db, final_state, user_id)
        yield f"data: {{ \"event\": \"completed\", \"scan_id\": {scan_id} }}\n\n"

@router.post("/url")
async def scan_url(scan_in: URLScanRequest, db: AsyncSession = Depends(get_db)):
    return StreamingResponse(event_generator(db, str(scan_in.target_url), "URL"), media_type="text/event-stream")
