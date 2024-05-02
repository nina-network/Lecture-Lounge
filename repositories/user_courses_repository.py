from repositories.db import get_pool
from psycopg.rows import dict_row

def get_all_user_courses():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT 
                                user_id,
                                course_id
                            FROM
                                user_courses;
                           ''')
            return cursor.fetchall()