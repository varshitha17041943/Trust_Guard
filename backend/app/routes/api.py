from fastapi import APIRouter
from app.controllers.auth_controller import router as auth_router
from app.controllers.scan_controller import router as scan_router
from app.controllers.user_controller import router as user_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="", tags=["auth"])
api_router.include_router(scan_router, prefix="/scan", tags=["scan"])
api_router.include_router(user_router, prefix="", tags=["user"])
