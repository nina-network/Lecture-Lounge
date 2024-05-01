CREATE TYPE role AS ENUM ('student', 'TA', 'admin');


CREATE TABLE IF NOT EXISTS users (
user_id SERIAL PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255),
email VARCHAR(255) NOT NULL UNIQUE,
username VARCHAR(255) NOT NULL UNIQUE,
user_role role NOT NULL,
user_pic VARCHAR(255),
password VARCHAR(255)
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



-- Inserting data into the users table

INSERT INTO users (first_name, last_name, email, username, user_role, password)
VALUES
    ('David', 'Wilson', 'david.wilson@example.com', 'davidwilson', 'student', 'password11'),
    ('Sarah', 'Anderson', 'sarah.anderson@example.com', 'sarahanderson', 'student', 'password12'),
    ('Ryan', 'Thomas', 'ryan.thomas@example.com', 'ryanthomas', 'student', 'password13'),
    ('Laura', 'Taylor', 'laura.taylor@example.com', 'laurataylor', 'student', 'password14'),
    ('Kevin', 'Roberts', 'kevin.roberts@example.com', 'kevinroberts', 'student', 'password15'),
    ('Hannah', 'Harris', 'hannah.harris@example.com', 'hannahharris', 'student', 'password16'),
    ('Daniel', 'Miller', 'daniel.miller@example.com', 'danielmiller', 'TA', 'password17'),
    ('Ava', 'Clark', 'ava.clark@example.com', 'avaclark', 'TA', 'password18'),
    ('Ethan', 'Wilson', 'ethan.wilson@example.com', 'ethanwilson', 'TA', 'password19'),
    ('Isabella', 'Moore', 'isabella.moore@example.com', 'isabellamoore', 'admin', 'password20');

-- Inserting data into the courses table
INSERT INTO courses (course_subject, course_number, course_name, description)
VALUES
    ('CS', 110, 'Introduction to Computer Science', 'Fundamentals of computer science concepts and programming.'),
    ('CS', 220, 'Database Systems', 'Design and implementation of database systems.'),
    ('CS', 330, 'Web Development Technologies', 'Advanced topics in web development and technologies.'),
    ('CS', 410, 'Data Structures', 'Study of fundamental data structures and their applications.'),
    ('CS', 510, 'Computer Networks', 'Introduction to computer networking principles and protocols.'),
    ('CS', 620, 'Machine Learning Foundations', 'Fundamental algorithms and methods in machine learning.'),
    ('CS', 730, 'Software Engineering Practices', 'Advanced software development methodologies and practices.'),
    ('CS', 820, 'Operating Systems Design', 'Design and implementation of operating systems.'),
    ('CS', 930, 'Cybersecurity Fundamentals', 'Introduction to cybersecurity principles and practices.'),
    ('CS', 1040, 'Mobile Application Development', 'Development of mobile applications using modern frameworks.');


-- Inserting data into the courses_prerequisites table
-- Inserting prerequisite relationships into the courses_prerequisites table
INSERT INTO courses_prerequisites (course_id, prerequisite_id)
VALUES
    (3, 1),   -- Web Development Technologies requires Introduction to Computer Science
    (4, 1),   -- Data Structures requires Introduction to Computer Science
    (4, 2),   -- Data Structures requires Database Systems
    (5, 1),   -- Computer Networks requires Introduction to Computer Science
    (6, 1),   -- Machine Learning Foundations requires Introduction to Computer Science
    (6, 4),   -- Machine Learning Foundations requires Data Structures
    (7, 3),   -- Software Engineering Practices requires Web Development Technologies
    (8, 6),   -- Operating Systems Design requires Machine Learning Foundations
    (10, 7);  -- Mobile Application Development requires Software Engineering Practices

-- Inserting data into the user_courses table
INSERT INTO user_courses (user_id, course_id)
VALUES
    (1, 1),    -- John is enrolled in Introduction to Computer Science
    (2, 2),    -- Jane is enrolled in Database Systems
    (3, 3),    -- Alice is enrolled in Web Development Technologies
    (4, 4),    -- Bob is enrolled in Data Structures
    (5, 5),    -- Michael is enrolled in Computer Networks
    (6, 6),    -- Emma is enrolled in Machine Learning Foundations
    (7, 7),    -- Matthew is enrolled in Software Engineering Practices
    (8, 8),    -- Olivia is enrolled in Operating Systems Design
    (9, 9),    -- William is enrolled in Cybersecurity Fundamentals
    (10, 10);  -- Sophia is enrolled in Mobile Application Development

-- Inserting data into the posts table

INSERT INTO posts (title, content, user_id, course_id)
VALUES
    ('Getting Started with Programming', 'Learn the basics of programming and start your coding journey!', 1, 1),   -- Introduction to Computer Science
    ('The Art of Coding', 'Discover the art of coding and its creative possibilities.', 2, 1),   -- Introduction to Computer Science
    ('SQL Essentials for Beginners', 'Begin your journey in SQL with fundamental concepts and queries.', 3, 2),   -- Database Systems
    ('Mastering Database Management', 'Take your database management skills to the next level.', 4, 2),   -- Database Systems
    ('Introduction to Web Development Technologies', 'Dive into web development with HTML, CSS, and JavaScript.', 5, 3),   -- Web Development Technologies
    ('Creating Responsive Websites', 'Learn how to build responsive and user-friendly websites.', 6, 3),   -- Web Development Technologies
    ('Exploring Data Structures and Algorithms', 'Explore the world of data structures and algorithms.', 7, 4),   -- Data Structures
    ('Demystifying Algorithms', 'Uncover the secrets behind efficient algorithms.', 8, 4),   -- Data Structures
    ('Fundamentals of Computer Networks', 'Gain insights into network protocols and architectures.', 9, 5),   -- Computer Networks
    ('Journey into Computer Networking', 'Embark on a fascinating journey through computer networking technologies.', 10, 5);   -- Computer Networks

-- Inserting data into the comments table
INSERT INTO comments (content, user_id, post_id)
VALUES
    ('Excited to learn more from you!', 1, 1),   -- Comment on post with ID 11 ("Getting Started with Programming")
    ('Great insights into database management.', 3, 2),   -- Comment on post with ID 12 ("The Art of Coding")
    ('Web development opens up new opportunities.', 5, 3),   -- Comment on post with ID 13 ("SQL Essentials for Beginners")
    ('Data structures are fascinating!', 7, 4),   -- Comment on post with ID 14 ("Mastering Database Management")
    ('Computer networks are the backbone of the internet.', 9, 5),   -- Comment on post with ID 15 ("Introduction to Web Development Technologies")
    ('Responsive web design is essential in today''s world.', 6, 6),   -- Comment on post with ID 16 ("Creating Responsive Websites")
    ('Agile methodologies are transforming software development.', 7, 7),   -- Comment on post with ID 17 ("Exploring Data Structures and Algorithms")
    ('Thanks for sharing this valuable information.', 8, 8),   -- Comment on post with ID 18 ("Demystifying Algorithms")
    ('Useful cybersecurity fundamentals!', 9, 9),   -- Comment on post with ID 19 ("Fundamentals of Computer Networks")
    ('Looking forward to more tutorials on computer networking.', 10, 10);   -- Comment on post with ID 20 ("Journey into Computer Networking")
