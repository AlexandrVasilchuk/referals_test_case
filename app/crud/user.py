from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import User
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_invited_user(self, referral_id: int, session: AsyncSession):
        query = await session.execute(
            select(User).where(User.invited_by == referral_id)
        )
        return query.scalars().all()


crud_user = CRUDUser(User)
