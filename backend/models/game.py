from datetime import date
from typing import Optional

from enums.game_enums import Platform, Status
from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


class Game(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=250)
    synopsis: Optional[str] = Field(default=None, max_length=1000)
    cover_url: Optional[str] = Field(default=None)
    status: Status = Field(default=Status.BACKLOG)
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    notes: Optional[str] = Field(default=None, max_length=450)
    platform: Platform
    genres: list[str] = Field(sa_column=Column(JSON))
    release_date: date
    date_completed: Optional[date] = None
