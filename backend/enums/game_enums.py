from enum import Enum


class Status(str, Enum):
    BACKLOG = "Backlog"
    PLAYING = "Playing"
    COMPLETED = "Completed"
    DROPPED = "Dropped"


class Platform(str, Enum):
    PLAYSTATION = "Playstation"
    SWITCH = "Switch"
    XBOX = "Xbox"
    PC = "PC"


class Genre(str, Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    RPG = "RPG"
    HORROR = "Horror"
    STRATEGY = "Strategy"
    SIMULATION = "Simulation"
    SPORTS = "Sports"
    PUZZLE = "Puzzle"
