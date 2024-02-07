from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    invited_by: int


class UserCreate(schemas.BaseUserCreate):
    referral_code: Optional[str]


class UserUpdate(schemas.BaseUserUpdate):
    pass
