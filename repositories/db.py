from psycopg_pool import ConnectionPool
import os

pool = None

def get_pool():
    global pool
    if pool is None:
        pool = ConnectionPool(
            conninfo=os.getenv('DATABASE_URL','')
        )
    return pool