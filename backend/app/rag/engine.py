class RAGService:
    def __init__(self):
        # In a real scenario, this connects to pgvector
        self.knowledge_base = [
            "Always verify website URLs before logging in.",
            "Never share One-Time Passwords (OTPs) with anyone.",
            "Typosquatting is when attackers use similar looking domains like amaz0n.com."
        ]
        
    def retrieve(self, query: str) -> str:
        # Mock semantic search
        return " ".join(self.knowledge_base)

rag_engine = RAGService()
