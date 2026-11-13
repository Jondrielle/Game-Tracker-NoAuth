from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class BaseGame(BaseModel):
    name: str
    status: str
    rating: int
    notes: Optional[str] = Field(default=None)
    platform: str
    genres: str
    release_date: date
    date_completed: Optional[date] = None


class ResponseGame(BaseGame):
    id: int
