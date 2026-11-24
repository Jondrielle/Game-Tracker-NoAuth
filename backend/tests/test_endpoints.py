import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy.engine import make_url
from sqlmodel import Session, SQLModel, create_engine

from backend.main import app
from backend.database import get_session
from backend.models.game import Game  # Registers the Game table with SQLModel


load_dotenv()

test_db_url = os.getenv("TEST_DATABASE_URL")
dev_db_url = os.getenv("DATABASE_URL")

if not test_db_url:
    raise RuntimeError("TEST_DATABASE_URL is not configured")

if test_db_url == dev_db_url:
    raise RuntimeError("Test database cannot be the same as development database")

if make_url(test_db_url).database != "game_tracker_test":
    raise RuntimeError("Tests must use game_tracker_test")


test_engine = create_engine(test_db_url)


def get_test_session():
    with Session(test_engine) as session:
        yield session


client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_test_database():
    SQLModel.metadata.create_all(test_engine)

    app.dependency_overrides[get_session] = get_test_session

    yield

    app.dependency_overrides.pop(get_session, None)
