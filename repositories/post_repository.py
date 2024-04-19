from repositories.db import get_pool
from psycopg.rows import dict_row


# get all posts by room
def get_all_posts():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM posts;')
            return cursor.fetchall()
