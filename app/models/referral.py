from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class ReferralCode(Base):
    code: Mapped[str] = mapped_column(String(length=16), unique=True)
    to_date: Mapped[datetime] = mapped_column(DateTime)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
