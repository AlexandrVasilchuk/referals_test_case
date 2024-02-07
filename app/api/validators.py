from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.referral import referral_code_crud

USER_ALREADY_HAVE_CODE = ("У вас уже создан реферальный код. "
                          "Удалите старый прежде, чем создавать новый")
USER_DOES_NOT_HAVE_CODE_YET = "У вас нет ни одного реферального кода."


async def referral_create(user_id: int, session: AsyncSession) -> None:
    code = await referral_code_crud.get_by_attribute(
        "owner_id", user_id, session
    )
    if code is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=USER_ALREADY_HAVE_CODE,
        )


async def referral_delete(user_id: int, session: AsyncSession) -> None:
    code = await referral_code_crud.get_by_attribute(
        "owner_id", user_id, session
    )
    if code is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=USER_DOES_NOT_HAVE_CODE_YET,
        )
