from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import referral_create, referral_delete
from app.core.authentication import current_user
from app.core.db import get_async_session
from app.crud.referral import referral_code_crud
from app.models import User
from app.schemas.referral import (ReferralCodeCreate, ReferralCodeDB,
                                  ReferralCodeRead)

router = APIRouter()


@router.post("/generate_referral", tags=["referral"])
async def generate_referral(
    new_referral: ReferralCodeCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    await referral_create(user.id, session)
    new_referral = await referral_code_crud.create(user, new_referral, session)
    await session.commit()
    await session.refresh(new_referral)
    return new_referral


@router.delete(
    "/delete_referral", tags=["referral"], response_model=ReferralCodeDB
)
async def delete_referral(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    await referral_delete(user.id, session)
    code_object = await referral_code_crud.get_by_attribute(
        "owner_id", user.id, session
    )
    await referral_code_crud.remove(code_object, session)
    return code_object


@router.post(
    "/get_referral_code",
    tags=["referral"],
    response_model=Optional[ReferralCodeDB],
)
async def get_referral(
    referral_read_schema: ReferralCodeRead,
    session: AsyncSession = Depends(get_async_session),
):
    return await referral_code_crud.get_code_by_user_attr(
        "email", referral_read_schema.owner_email, session
    )
