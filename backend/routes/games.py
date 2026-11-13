from fastapi import APIRouter

game_router = APIRouter()

# Get all games
@game_router.get("/")
async def get_games():
    return {"message": "Return all games"}

# Get a game
@game_router.get("/{id}")
async def get_game():
    return {"message": "Retrieved game successfully"}

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
    return {"message" : "Updated Game Successfully"}