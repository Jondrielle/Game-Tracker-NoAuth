import pytest
from database import engine
from sqlalchemy import text


@pytest.mark.skip(reason="Waiting for test database setup")
def test_database_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(result.scalar())
