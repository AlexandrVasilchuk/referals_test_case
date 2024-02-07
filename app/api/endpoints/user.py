from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.authentication import auth_backend, fastapi_users
from app.core.db import get_async_session
from app.crud.user import crud_user
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/invited_by/{referral_user_id}",
    tags=["users", "referral"],
    response_model=List[UserRead],
)
async def get_invited_users(
    referral_user_id: int, session: AsyncSession = Depends(get_async_session)
):
    return await crud_user.get_invited_user(referral_user_id, session)
