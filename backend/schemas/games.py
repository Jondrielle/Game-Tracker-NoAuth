from datetime import date
from typing import Optional

from enums.game_enums import Genre, Platform, Status
from pydantic import BaseModel, Field


class BaseGame(BaseModel):
    name: str = Field(max_length=250)
    status: Status
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    notes: Optional[str] = Field(default=None)
    platform: Platform
    genres: list[Genre]
    release_date: date
    date_completed: Optional[date] = None


class ResponseGame(BaseGame):
    id: int
