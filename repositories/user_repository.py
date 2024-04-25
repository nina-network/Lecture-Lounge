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


def create_user(first_name: str, last_name: str, email: str, username: str, password: str) -> dict[str, Any]:
    default_role = 'student'
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        INSERT INTO users (first_name, last_name, email, username, user_role, password)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        RETURNING user_id
                        ''', [first_name, last_name, email, username, default_role, password]
                        )
            user_id = cur.fetchone()
            if user_id is None:
                raise Exception('failed to create user')
            return {
                'user_id': user_id,
                'username': username
            }
        
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