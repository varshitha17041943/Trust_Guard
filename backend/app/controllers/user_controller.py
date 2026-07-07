from fastapi import APIRouter

router = APIRouter()

@router.get("/profile")
async def get_profile():
    return {"email": "admin@trustguard.ai", "role": "admin", "is_active": True}

@router.get("/settings")
async def get_settings():
    return {"theme": "dark", "notifications_enabled": True, "aggressive_scan": False}

@router.get("/history")
async def get_history():
    return [{"id": 1, "target": "https://example.com", "risk_score": 2.0}]

@router.get("/report")
async def get_report():
    return {"status": "generated", "url": "/downloads/report_1.pdf"}
