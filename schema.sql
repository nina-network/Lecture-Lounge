
CREATE TYPE role AS ENUM ('student', 'TA', 'admin');

CREATE TABLE IF NOT EXISTS users (
    user_id     SERIAL PRIMARY KEY,
    first_name   VARCHAR(255),
    last_name    VARCHAR(255),
    email       VARCHAR(255) NOT NULL UNIQUE,
    username    VARCHAR(255) NOT NULL UNIQUE,
    user_role   role NOT NULL,
    password    VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS courses (
    course_id   SERIAL PRIMARY KEY,
    course_subject VARCHAR(255) NOT NULL,
    course_number INT NOT NULL,
    course_name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_courses (
    user_id     SERIAL NOT NULL,
    course_id   SERIAL NOT NULL,
    FOREIGN KEY (user_id)    REFERENCES users(user_id),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)
);

CREATE TABLE IF NOT EXISTS courses_prerequisites (
    course_id         INT NOT NULL,
    prerequisite_id   INT NOT NULL,
    FOREIGN KEY (course_id)       REFERENCES courses(course_id),
    FOREIGN KEY (prerequisite_id) REFERENCES courses(course_id)
);

CREATE TABLE IF NOT EXISTS posts (
    post_id     SERIAL PRIMARY KEY,
    title       VARCHAR(255) NOT NULL,
    content     TEXT NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id     INT NOT NULL,
    course_id   INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE IF NOT EXISTS comments (
    comment_id  SERIAL PRIMARY KEY,
    content     TEXT NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id     INT NOT NULL,
    post_id     INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);