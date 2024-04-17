-- Inserting data into the users table
INSERT INTO users (firstName, lastName, email, username, password)
VALUES
    ('John', 'Doe', 'john.doe@example.com', 'johndoe', 'password1'),
    ('Jane', 'Smith', 'jane.smith@example.com', 'janesmith', 'password2'),
    ('Alice', 'Johnson', 'alice.johnson@example.com', 'alicejohnson', 'password3'),
    ('Bob', 'Brown', 'bob.brown@example.com', 'bobbrown', 'password4'),
    ('Michael', 'Williams', 'michael.williams@example.com', 'michaelwilliams', 'password5'),
    ('Emma', 'Jones', 'emma.jones@example.com', 'emmajones', 'password6'),
    ('Matthew', 'Davis', 'matthew.davis@example.com', 'matthewdavis', 'password7'),
    ('Olivia', 'Martinez', 'olivia.martinez@example.com', 'oliviamartinez', 'password8'),
    ('William', 'Rodriguez', 'william.rodriguez@example.com', 'williamrodriguez', 'password9'),
    ('Sophia', 'Garcia', 'sophia.garcia@example.com', 'sophiagarcia', 'password10');

-- Inserting data into the courses table
INSERT INTO courses (course_name, description)
VALUES
    ('Introduction to Programming', 'Learn the basics of programming concepts.'),
    ('Database Management Systems', 'Introduction to database design and management.'),
    ('Web Development', 'Learn about web development technologies and frameworks.'),
    ('Data Structures and Algorithms', 'Study common data structures and algorithms.'),
    ('Computer Networks', 'Explore the fundamentals of computer networks.');

-- Inserting data into the courses_prerequisites table
INSERT INTO courses_prerequisites (course_id, prerequisite_id)
VALUES
    (3, 1),  -- Web Development requires Introduction to Programming
    (4, 1),  -- Data Structures and Algorithms requires Introduction to Programming
    (4, 2),  -- Data Structures and Algorithms requires Database Management Systems
    (5, 1);  -- Computer Networks requires Introduction to Programming

-- Inserting data into the posts table
INSERT INTO posts (title, content, user_id, course_id)
VALUES
    ('Introduction to Programming', 'Welcome to the world of programming!', 1, 1),
    ('SQL Basics', 'Learn the fundamentals of SQL.', 2, 2),
    ('Building a Basic Website', 'Get started with building your first website.', 3, 3),
    ('Sorting Algorithms', 'Explore different sorting algorithms.', 4, 4),
    ('Introduction to Networking', 'Learn about computer networking concepts.', 5, 5);

-- Inserting data into the comments table
INSERT INTO comments (content, user_id, post_id)
VALUES
    ('Great post!', 6, 1),
    ('Looking forward to more!', 7, 2),
    ('Nice tutorial!', 8, 3),
    ('Very informative.', 9, 4),
    ('Thanks for sharing!', 10, 5);

-- Inserting more data into the courses table
INSERT INTO courses (course_name, description)
VALUES
    ('Machine Learning', 'Introduction to machine learning algorithms and techniques.'),
    ('Software Engineering', 'Study software development methodologies and practices.'),
    ('Operating Systems', 'Learn about operating system concepts and design.'),
    ('Computer Security', 'Introduction to computer security principles.'),
    ('Mobile App Development', 'Explore mobile application development frameworks.');

-- Inserting more data into the posts table
INSERT INTO posts (title, content, user_id, course_id)
VALUES
    ('Regression Analysis', 'Understanding linear regression and its applications in machine learning.', 2, 6),
    ('Agile Development', 'Overview of agile software development methodologies.', 3, 7),
    ('Memory Management', 'Exploring memory management techniques in operating systems.', 4, 8),
    ('Encryption Basics', 'Introduction to encryption techniques and algorithms.', 5, 9),
    ('Android Development', 'Getting started with Android app development using Java.', 1, 10);

-- Inserting more data into the comments table
INSERT INTO comments (content, user_id, post_id)
VALUES
    ('This helped me a lot!', 6, 6),
    ('Nice overview of agile!', 7, 7),
    ('Thanks for sharing.', 8, 8),
    ('Very useful information!', 9, 9),
    ('Looking forward to more tutorials!', 10, 10);