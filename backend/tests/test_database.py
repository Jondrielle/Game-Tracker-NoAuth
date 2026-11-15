import pytest


@pytest.mark.skip(reason="Waiting for test database setup")
def test_database_connection():
    from sqlalchemy import text

    from backend.database import engine

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1
