from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.games import game_router

app = FastAPI()

origins = ["https://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(game_router)
