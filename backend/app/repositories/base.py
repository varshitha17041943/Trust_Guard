from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Generic, TypeVar, Type
from app.models.base import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: int) -> ModelType | None:
        result = await db.execute(select(self.model).filter(self.model.id == id))
        return result.scalars().first()

    async def create(self, db: AsyncSession, obj_in: dict) -> ModelType:
        obj_data = self.model(**obj_in)
        db.add(obj_data)
        await db.commit()
        await db.refresh(obj_data)
        return obj_data
