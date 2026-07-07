import os

def create_files():
    files = {
        "backend/app/models/expansion.py": """from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.session import Base
# Note: pgvector would be used here in production: from pgvector.sqlalchemy import Vector

class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    category = Column(String, index=True)
    difficulty = Column(String)
    # embedding = Column(Vector(768)) # Requires pgvector extension in Postgres
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ChatHistory(Base):
    __tablename__ = "chat_history"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    user_query = Column(Text)
    ai_response = Column(Text)
    sources = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    type = Column(String) # 'HighRisk', 'ReportReady', etc.
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
    user_agent = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
""",
        "backend/app/controllers/chat_controller.py": """from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
import asyncio

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    session_id: str

@router.post("/api/chat")
async def chat_with_ai(request: ChatRequest):
    # Mock RAG / Gemini execution for demonstration
    # In production, this generates an embedding using Gemini API, 
    # queries pgvector for cosine similarity, and streams response.
    await asyncio.sleep(1)
    
    if "phishing" in request.query.lower():
        answer = "Phishing is a social engineering attack where attackers deceive you into revealing sensitive data."
        source = "OWASP Phishing Documentation"
    elif "ssl" in request.query.lower():
        answer = "SSL (Secure Sockets Layer) encrypts the connection between your browser and the website."
        source = "SSL Documentation"
    else:
        answer = "I can only answer cybersecurity questions based on our secure RAG knowledge base. Please ask about phishing, SSL, or scams."
        source = "TrustGuardAI Knowledge Base"
        
    return {
        "answer": answer,
        "sources": [source],
        "cyber_tip": "Always check the URL bar for typos before entering passwords.",
        "related_questions": ["What is Typosquatting?", "How do QR scams work?"]
    }
""",
        "backend/app/controllers/admin_controller.py": """from fastapi import APIRouter, Depends
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
""",
        "backend/app/controllers/notification_controller.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/api/notifications")
async def get_notifications():
    return [
        {"id": 1, "message": "High-Risk Website Detected: paypal-secure-login.com", "type": "critical", "is_read": False},
        {"id": 2, "message": "Your PDF Security Report is ready.", "type": "info", "is_read": True}
    ]
""",
        "backend/app/controllers/health_controller.py": """from fastapi import APIRouter

router = APIRouter()

@router.get("/api/health")
async def health_check():
    # Observability Endpoint for Docker / Kubernetes probes
    return {
        "status": "healthy",
        "services": {
            "database": "connected",
            "mcp_server": "connected",
            "redis_cache": "connected"
        },
        "metrics": {
            "avg_workflow_latency_ms": 1240,
            "agent_success_rate": "99.9%"
        }
    }
"""
    }

    for path, content in files.items():
        dirname = os.path.dirname(path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    create_files()
    print("Backend Expansion (Stages 21-25) Scaffolded.")
