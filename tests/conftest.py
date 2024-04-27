import pytest 
from repositories.db import get_pool
from psycopg.rows import dict_row
from app import app

@pytest.fixture(scope='module')
def test_app():
    return app.test_client()

@pytest.fixture(scope='session')
def test_database_url():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            DROP SCHEMA public CASCADE;
                            CREATE SCHEMA public;
                            ''')
            # drop tables and types
            with open("schema.sql") as file:
                cursor.executescript(file.read())
            with open("insert.sql") as file:
                cursor.executescript(file.read())