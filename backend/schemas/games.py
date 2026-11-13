from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class BaseGame(BaseModel):
    name: str
    status: str
    rating: int
    notes: Optional[str] = Field(default=None)
    platform: str
    genres: str
    release_date: date
    date_completed: Optional[date] = Field(default=None) 

class ResponseGame(BaseGame):
    id: int
