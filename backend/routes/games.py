from typing import Annotated

from database import get_session
from fastapi import APIRouter, Depends, HTTPException
from models.game import Game as GameModel
from schemas.games import ResponseGame
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
@game_router.post("/game")
async def create_game():
    return {"message": "Game Created Successfully"}


# Delete a game
@game_router.delete("/game/{id}")
async def delete_game():
    return {"message": "Delete Game Successfully"}


# Clear all games
@game_router.delete("/game")
async def clear_games():
    return {"message": "Clear games"}


# Update a game
@game_router.patch("/game/{id}")
async def update_game():
    return {"message": "Updated Game Successfully"}
