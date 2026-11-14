from sqlmodel import Field, SQLModel


class Game(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
