import secrets
from datetime import datetime, timedelta

from sqlalchemy import join, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import ReferralCode, User
from app.schemas.referral import ReferralCodeCreate


class CRUDReferral(CRUDBase[ReferralCode, ReferralCodeCreate, None]):
    async def create(
        self,
        user: User,
        create_schema: ReferralCodeCreate,
        session: AsyncSession,
    ) -> ReferralCode:
        object_data = create_schema.dict()
        days = object_data.pop("duration_days")
        object_data.update(
            owner_id=user.id,
            to_date=datetime.now() + timedelta(days=days),
            code=secrets.token_hex(8),
        )
        new_object = self.model(**object_data)
        session.add(new_object)
        return new_object

    async def get_code_by_user_attr(
        self, attribute_name: str, attribute_value: str, session: AsyncSession
    ) -> ReferralCode:
        statement = join(User, ReferralCode, User.id == ReferralCode.owner_id)
        attribute = getattr(User, attribute_name)
        referral_code = await session.execute(
            select(ReferralCode)
            .select_from(statement)
            .where(attribute == attribute_value)
        )
        return referral_code.scalars().first()


referral_code_crud = CRUDReferral(ReferralCode)
