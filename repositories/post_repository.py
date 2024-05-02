from repositories.db import get_pool
from psycopg.rows import dict_row


# get all posts by room
def get_all_posts():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('SELECT * FROM posts;')
            return cursor.fetchall()

def get_post_by_title(title):
    pool = get_pool()
    with pool.connection() as conn: 
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT 
                                title,
                                content,
                                user_id,
                                course_id
                            FROM
                                posts
                            WHERE
                                title = %s
                            ''', [title])
            return cursor.fetchone()

def get_post_by_course_id(course_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT  
                            title,
                            content,
                            user_id,
                            course_id
                        FROM
                            posts
                        WHERE 
                            course_id = %s
                        ''', [course_id])
            return cur.fetchall()
        
def create_new_post(title, content, user_id, course_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            INSERT INTO 
                                posts (title, content, user_id, course_id)
                            VALUES  
                                (%s, %s, %s, %s)
                            ''', [title, content, user_id, course_id])
            
def get_post_by_user_id(user_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            title,
                            content,
                            user_id,
                            course_id
                        FROM
                            posts
                        WHERE
                            user_id = %s
                        ''', [user_id])
            user_posts = cur.fetchall()
        return user_posts
    
def delete_post_by_title(title):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute('DELETE FROM comments WHERE post_id IN (SELECT post_id FROM posts WHERE title = %s)', [title])
                cur.execute('DELETE FROM posts WHERE title = %s', [title])
                
                conn.commit()
                return True
            except Exception as e:
                print(f"Error deleting post: {e}")
                conn.rollback()
                return False