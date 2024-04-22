-- Inserting data into the users table
INSERT INTO users (firstName, lastName, email, username, password)
VALUES 
    ('John', 'Doe', 'john.doe@example.com', 'johndoe', 'password123'),
    ('Jane', 'Smith', 'jane.smith@example.com', 'janesmith', 'qwerty'),
    ('Alice', 'Johnson', 'alice.johnson@example.com', 'alicej', 'securepass'),
    ('Michael', 'Brown', 'michael.brown@example.com', 'michaelb', 'brown123'),
    ('Emily', 'Davis', 'emily.davis@example.com', 'emilyd', 'davis456'),
    ('David', 'Martinez', 'david.martinez@example.com', 'davidm', 'martinez789'),
    ('Sarah', 'Wilson', 'sarah.wilson@example.com', 'sarahw', 'wilsonabc'),
    ('Matthew', 'Anderson', 'matthew.anderson@example.com', 'matthewa', 'andersonxyz'),
    ('Jessica', 'Taylor', 'jessica.taylor@example.com', 'jessicat', 'taylor123'),
    ('Daniel', 'Thomas', 'daniel.thomas@example.com', 'danielt', 'thomas456');

-- Inserting data into the courses table
INSERT INTO courses (course_subject, course_number, course_name, description)
VALUES 
    ('Math', 101, 'Introduction to Calculus', 'This course provides an introduction to differential and integral calculus.'),
    ('History', 201, 'World History: Ancient Civilizations', 'Explore the ancient civilizations of the world from Mesopotamia to Rome.'),
    ('Computer Science', 301, 'Introduction to Python Programming', 'Learn the fundamentals of programming using the Python language.'),
    ('Biology', 101, 'Introduction to Biology', 'An introductory course covering the basics of biology and life sciences.'),
    ('Literature', 201, 'World Literature: Modern Classics', 'Exploring modern classic literature from around the world.'),
    ('Physics', 301, 'Mechanics and Motion', 'Study of the principles of mechanics and motion.'),
    ('Chemistry', 201, 'Organic Chemistry', 'Introduction to the structure, properties, and reactions of organic compounds.');

-- Inserting data into the courses_prerequisites table
INSERT INTO courses_prerequisites (course_id, prerequisite_id)
VALUES 
    (4, 1), -- Organic Chemistry has a prerequisite of Introduction to Biology
    (3, 1), -- Mechanics and Motion has a prerequisite of Introduction to Biology
    (4, 5), -- Organic Chemistry has a prerequisite of World Literature: Modern Classics
    (3, 5); -- Mechanics and Motion has a prerequisite of World Literature: Modern Classics

-- Inserting data into the posts table
INSERT INTO posts (title, content, user_id, course_id)
VALUES 
    ('First Post', 'This is the content of the first post.', 1, 1),
    ('Python Question', 'I have a question about loops in Python.', 2, 3),
    ('Ancient Rome', 'Let''s discuss the rise and fall of the Roman Empire.', 3, 2),
    ('Math Help Needed', 'Can someone help me with derivatives?', 4, 1),
    ('Egyptian Civilization', 'Exploring the mysteries of ancient Egypt.', 5, 2),
    ('Python Project Ideas', 'Share your ideas for Python projects!', 6, 3),
    ('Interesting History Fact', 'Did you know about the Battle of Marathon?', 7, 2),
    ('Linear Algebra Question', 'Struggling with matrix multiplication.', 8, 1),
    ('Medieval Europe', 'Discussing feudalism and knights.', 9, 2),
    ('Debugging Help', 'My Python code isn''t working, need assistance.', 10, 3);

-- Inserting data into the comments table
INSERT INTO comments (content, user_id, post_id)
VALUES 
    ('Great post! Looking forward to more.', 2, 1),
    ('For loops or while loops?', 1, 2),
    ('I find Roman history fascinating!', 1, 3),
    ('I can help with derivatives.', 5, 4),
    ('I love learning about ancient civilizations.', 6, 5),
    ('How about a web scraping project?', 7, 6),
    ('Yes, it was a decisive battle in Greek history.', 8, 7),
    ('I can explain matrix multiplication.', 9, 8),
    ('Feudalism is such an interesting topic.', 10, 9),
    ('Sure, what seems to be the problem?', 2, 10);
