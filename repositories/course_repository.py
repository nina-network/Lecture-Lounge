from repositories.db import get_pool
from psycopg.rows import dict_row


# get all the rooms
def get_all_courses():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT 
                                course_id,
                                course_name
                            FROM
                                courses;
                           ''')
            return cursor.fetchall()
        
# get room by id
def get_course_by_id(course_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute('''
                            SELECT 
                                course_id,
                                course_subject,
                                course_number,
                                course_name,
                                description
                            FROM
                                courses
                            WHERE
                                course_id = %s;
                           ''', (course_id,))
            return cursor.fetchone()

def create_course(course):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO courses (course_subject, course_number, course_name, description)
                VALUES (%s, %s, %s, %s)
            ''', (course.get('course_subject', 'Default Subject'), course.get('course_number', 0), course['course_name'], course['description']))
            conn.commit()

def get_all_course_ids():
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        SELECT 
                            course_id
                        FROM
                            courses
                        ''')
            return[row[0] for row in cur.fetchall()]
        
def get_course_name_by_id(course_id):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                        SELECT
                            course_name
                        FROM
                            courses
                        WHERE
                            course_id = %s
                        ''', [course_id])
            course_name = cur.fetchone()
            return course_name

def get_course_name(course_name):
    pool = get_pool()
    with pool.connection() as conn:
        with conn.cursor() as cur: 
            cur.execute('''
                        SELECT 
                            course_name
                        FROM 
                            courses
                        ''')
            course_name = cur.fetchone()
            return course_name