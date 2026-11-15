from typing import Annotated

from database import get_session
from fastapi import APIRouter, Depends, HTTPException
from models.game import Game as GameModel
from schemas.games import CreateGame, ResponseGame
from sqlmodel import Session, select

sessionDeps = Annotated[Session, Depends(get_session)]

game_router = APIRouter()


# Get all games
@game_router.get("/", response_model=list[ResponseGame])
async def get_games(session: sessionDeps):
    statement = select(GameModel)
    return session.exec(statement).all()


# Get a game
@game_router.get("/{id}", response_model=ResponseGame)
async def get_game(id: int, session: sessionDeps):
    statement = select(GameModel).where(GameModel.id == id)

    game = session.exec(statement).first()

    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    return game


# Create a game
@game_router.post("/game", response_model=ResponseGame)
async def create_game(new_game: CreateGame, session: sessionDeps):
    current_game = GameModel(
        igdb_id=new_game.igdb_id,
        name=new_game.name,
        synopsis=new_game.synopsis,
        cover_url=new_game.cover_url,
        status=new_game.status,
        rating=new_game.rating,
        notes=new_game.notes,
        platform=new_game.platform,
        genres=[genre.value for genre in new_game.genres],
        release_date=new_game.release_date,
        date_completed=new_game.date_completed,
    )

    session.add(current_game)
    session.commit()
    session.refresh(current_game)

    return current_game


# Delete a game
@game_router.delete("/game/{id}")
async def delete_game(id: int, session: sessionDeps):
    statement = select(GameModel).where(GameModel.id == id)

    game = session.exec(statement).first()

    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    session.delete(game)
    session.commit()

    return {"message": "Deleted Game Successfully"}


# Clear all games
@game_router.delete("/game")
async def clear_games():
    return {"message": "Clear games"}


# Update a game
@game_router.patch("/game/{id}")
async def update_game():
    return {"message": "Updated Game Successfully"}
