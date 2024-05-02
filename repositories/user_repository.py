from typing import Any
from repositories.db import get_pool
from psycopg.rows import dict_row

def does_username_exist(username: str) -> bool:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        SELECT
                            user_id
                        FROM
                            users
                        WHERE username = %s
                        ''', [username])
            user_id = cur.fetchone()
            return user_id is not None


def create_user(first_name: str, last_name: str, email: str, role: str, username: str, password: str) -> dict[str, Any]:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        INSERT INTO users (first_name, last_name, email, username, user_role, password)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        RETURNING user_id
                        ''', [first_name, last_name, email, username, role, password]
                        )
            user_id = cur.fetchone()
            if user_id is None:
                raise Exception('failed to create user')
            return {
                'user_id': user_id,
                'username': username
            }
        
def create_oauth_user(first_name: str, last_name: str, username: str, role: str, email: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        INSERT INTO users (first_name, last_name, email, username, user_role)
                        VALUES (%s, %s, %s, %s, %s)
                        RETURNING user_id
                        ''', [first_name, last_name, email, username, role]
                        )
            user_id = cur.fetchone()
            if user_id is None:
                raise Exception('failed to create user')

        
def get_user_by_email(email: str) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            user_id,
                            username,
                            password AS hashed_password
                        FROM
                            users
                        WHERE email = %s
                        ''', [email])
            user = cur.fetchone()
            return user
        
def get_user_id_by_email(email: str) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            user_id
                        FROM
                            users
                        WHERE 
                            email = %s
                        ''', [email])
            user_id = cur.fetchone()
            return user_id

def get_user_by_username(username: str) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            user_id,
                            username,
                            password AS hashed_password
                        FROM
                            users
                        WHERE username = %s
                        ''', [username])
            user = cur.fetchone()
            return user


def get_user_by_id(user_id: int) -> dict[str, Any] | None:
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            user_id,
                            username
                        FROM
                            users
                        WHERE user_id = %s
                        ''', [user_id])
            user = cur.fetchone()
            return user
        
def get_all_users():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            *
                        FROM
                            users
                        ''')
            return cur.fetchall()
        
def set_profile_picture(user_id: int, pic_url: str):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        UPDATE 
                            users
                        SET 
                            user_pic = %s
                        WHERE 
                            user_id = %s
                        ''', [pic_url, user_id])
            
def get_profile_picture(user_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('''
                        SELECT
                            user_pic
                        FROM
                            users
                        WHERE
                            user_id = %s

                        ''', [user_id])
            row = cur.fetchone()
        print("row retrieved:", row)
        return row      