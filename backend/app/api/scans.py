from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.schemas.scan import ScanCreate
from app.workflows.engine import antigravity_scan_workflow

router = APIRouter()

@router.post("/stream")
async def stream_scan(scan_in: ScanCreate):
    return StreamingResponse(
        antigravity_scan_workflow(scan_in.target_url),
        media_type="text/event-stream"
    )
