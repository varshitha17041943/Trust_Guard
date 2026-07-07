from fastapi import APIRouter

router = APIRouter()

@router.get("/api/notifications")
async def get_notifications():
    return [
        {"id": 1, "message": "High-Risk Website Detected: paypal-secure-login.com", "type": "critical", "is_read": False},
        {"id": 2, "message": "Your PDF Security Report is ready.", "type": "info", "is_read": True}
    ]
