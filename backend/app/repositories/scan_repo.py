from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.scan import Scan
from app.models.embedding import Embedding
from .base import BaseRepository
from typing import List
import logging

logger = logging.getLogger(__name__)

class ScanRepository(BaseRepository[Scan]):
    def __init__(self):
        super().__init__(Scan)
        
    async def get_history_by_user(self, db: AsyncSession, user_id: int) -> List[Scan]:
        result = await db.execute(select(self.model).filter(self.model.user_id == user_id).order_by(self.model.created_at.desc()))
        return result.scalars().all()

    async def get_similar_scans(self, db: AsyncSession, vector: list, limit: int = 5):
        # Fallback for SQLite (returns recent scans instead of vector search)
        try:
            stmt = select(Scan).join(Embedding).order_by(Scan.created_at.desc()).limit(limit)
            result = await db.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            logger.error(f"Failed pgvector similarity search: {e}")
            return []

scan_repo = ScanRepository()
