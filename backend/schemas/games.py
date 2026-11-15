from datetime import date
from typing import Optional

from enums.game_enums import Genre, Platform, Status
from pydantic import BaseModel, Field


class BaseGame(BaseModel):
    igdb_id: Optional[int] = None
    name: str = Field(min_length=1, max_length=250)
    synopsis: Optional[str] = Field(default=None, max_length=1000)
    cover_url: Optional[str] = Field(default=None)
    status: Status = Field(default=Status.BACKLOG)
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    notes: Optional[str] = Field(default=None, max_length=450)
    platform: Platform
    genres: list[Genre]
    release_date: date
    date_completed: Optional[date] = None


class ResponseGame(BaseGame):
    id: int


class CreateGame(BaseGame):
    pass


class UpdateGame(BaseModel):
    igdb_id: Optional[int] = None
    name: Optional[str] = Field(default=None, min_length=1, max_length=250)
    synopsis: Optional[str] = Field(default=None, max_length=1000)
    cover_url: Optional[str] = Field(default=None)
    status: Optional[Status] = Field(default=None)
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    notes: Optional[str] = Field(default=None, max_length=450)
    platform: Optional[Platform] = Field(default=None)
    genres: Optional[list[Genre]] = Field(default=None)
    release_date: Optional[date] = Field(default=None)
    date_completed: Optional[date] = Field(default=None)
