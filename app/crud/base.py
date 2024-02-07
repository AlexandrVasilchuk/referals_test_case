from typing import Generic, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_by_attribute(
        self, attribute_name: str, attribute_value: str, session: AsyncSession
    ):
        attribute = getattr(self.model, attribute_name)
        db_object = await session.execute(
            select(self.model).where(attribute == attribute_value)
        )
        return db_object.scalars().first()

    async def remove(
        self, db_object: ModelType, session: AsyncSession
    ) -> ModelType:
        await session.delete(db_object)
        await session.commit()
        return db_object
