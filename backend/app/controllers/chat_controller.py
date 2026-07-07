from fastapi import APIRouter, Depends, Body
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
