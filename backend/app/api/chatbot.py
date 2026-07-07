from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.engine import rag_engine

router = APIRouter()

class ChatQuery(BaseModel):
    query: str

@router.post("/ask")
async def ask_chatbot(request: ChatQuery):
    context = rag_engine.retrieve(request.query)
    # In production, this would call Gemini with the context
    answer = f"Based on TrustGuard's knowledge base: {context} Remember to always stay vigilant online!"
    return {"answer": answer}
