from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class ReferralCodeDB(BaseModel):
    id: int
    code: str
    to_date: datetime


class ReferralCodeCreate(BaseModel):
    duration_days: Optional[int] = 7


class ReferralCodeRead(BaseModel):
    owner_email: EmailStr
