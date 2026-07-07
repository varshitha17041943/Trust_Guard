from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import auth_controller, scan_controller, report_controller, analytics_controller
from app.middleware.auth import JWTAuthMiddleware

app = FastAPI(title="TrustGuardAI Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_controller.router, prefix="/api/auth", tags=["auth"])
app.include_router(scan_controller.router, prefix="/api/scan", tags=["scans"])
app.include_router(report_controller.router, tags=["reports"])
app.include_router(analytics_controller.router, tags=["analytics"])

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
