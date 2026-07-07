from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from .base import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)
        
    async def get_by_email(self, db: AsyncSession, email: str) -> User | None:
        result = await db.execute(select(self.model).filter(self.model.email == email))
        return result.scalars().first()

user_repo = UserRepository()
