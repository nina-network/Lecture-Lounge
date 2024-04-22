-- Inserting data into the users table
INSERT INTO users (first_name, last_name, email, username, user_role, password)
VALUES
    ('John', 'Doe', 'john.doe@example.com', 'johndoe', 'student', 'password1'),
    ('Jane', 'Smith', 'jane.smith@example.com', 'janesmith', 'student', 'password2'),
    ('Alice', 'Johnson', 'alice.johnson@example.com', 'alicejohnson', 'student', 'password3'),
    ('Bob', 'Brown', 'bob.brown@example.com', 'bobbrown', 'student', 'password4'),
    ('Michael', 'Williams', 'michael.williams@example.com', 'michaelwilliams', 'student', 'password5'),
    ('Emma', 'Jones', 'emma.jones@example.com', 'emmajones', 'student', 'password6'),
    ('Matthew', 'Davis', 'matthew.davis@example.com', 'matthewdavis', 'TA', 'password7'),
    ('Olivia', 'Martinez', 'olivia.martinez@example.com', 'oliviamartinez', 'TA', 'password8'),
    ('William', 'Rodriguez', 'william.rodriguez@example.com', 'williamrodriguez', 'TA', 'password9'),
    ('Sophia', 'Garcia', 'sophia.garcia@example.com', 'sophiagarcia', 'admin', 'password10');

-- Inserting data into the courses table
INSERT INTO courses (course_subject, course_number, course_name, description)
VALUES
    ('CS', 101, 'Introduction to Programming', 'Learn the basics of programming concepts.'),
    ('CS', 201, 'Database Management Systems', 'Introduction to database design and management.'),
    ('CS', 301, 'Web Development', 'Learn about web development technologies and frameworks.'),
    ('CS', 401, 'Data Structures and Algorithms', 'Study common data structures and algorithms.'),
    ('CS', 501, 'Computer Networks', 'Explore the fundamentals of computer networks.'),
    ('CS', 601, 'Machine Learning', 'Introduction to machine learning algorithms and techniques.'),
    ('CS', 701, 'Software Engineering', 'Study software development methodologies and practices.'),
    ('CS', 801, 'Operating Systems', 'Learn about operating system concepts and design.'),
    ('CS', 901, 'Computer Security', 'Introduction to computer security principles.'),
    ('CS', 1001, 'Mobile App Development', 'Explore mobile application development frameworks.');

-- Inserting data into the courses_prerequisites table
INSERT INTO courses_prerequisites (course_id, prerequisite_id)
VALUES
    (3, 1),  -- Web Development requires Introduction to Programming
    (4, 1),  -- Data Structures and Algorithms requires Introduction to Programming
    (4, 2),  -- Data Structures and Algorithms requires Database Management Systems
    (5, 1),  -- Computer Networks requires Introduction to Programming
    (6, 1),  -- Machine Learning requires Introduction to Programming
    (6, 4),  -- Machine Learning requires Data Structures and Algorithms
    (7, 3),  -- Software Engineering requires Web Development
    (8, 6),  -- Operating Systems requires Machine Learning
    (10, 7);  -- Mobile App Development requires Software Engineering

-- Inserting data into the user_courses table
INSERT INTO user_courses (user_id, course_id)
VALUES
    (1, 1),  -- John is enrolled in Introduction to Programming
    (2, 2),  -- Jane is enrolled in Database Management Systems
    (3, 3),  -- Alice is enrolled in Web Development
    (4, 4),  -- Bob is enrolled in Data Structures and Algorithms
    (5, 5),  -- Michael is enrolled in Computer Networks
    (6, 6),  -- Emma is enrolled in Machine Learning
    (7, 7),  -- Matthew is enrolled in Software Engineering
    (8, 8),  -- Olivia is enrolled in Operating Systems
    (9, 9),  -- William is enrolled in Computer Security
    (10, 10);  -- Sophia is enrolled in Mobile App Development

-- Inserting data into the posts table
INSERT INTO posts (title, content, user_id, course_id)
VALUES
    ('Welcome to Programming 101', 'Welcome to the world of programming!', 1, 1),
    ('The Joy of Coding', 'Learning programming can be fun and challenging.', 2, 1),
    ('Mastering SQL Basics', 'Understanding SQL is crucial for managing databases.', 3, 2),
    ('Database Management Essentials', 'Relational databases play a key role in modern applications.', 4, 2),
    ('Introduction to Web Development', 'Get started with HTML, CSS, and JavaScript!', 5, 3),
    ('Building Responsive Websites', 'Building responsive web applications is an essential skill.', 6, 3),
    ('Exploring Data Structures', 'Explore different data structures like arrays, linked lists, and trees.', 7, 4),
    ('Algorithms Demystified', 'Efficient algorithms are the heart of computer science.', 8, 4),
    ('Network Fundamentals', 'Understanding network protocols and architectures.', 9, 5),
    ('Journey Through Computer Networks', 'Explore how the internet works and its underlying technologies.', 10, 5);


-- Inserting data into the comments table
INSERT INTO comments (content, user_id, post_id)
VALUES
    ('Great post! Looking forward to more.', 1, 1),
    ('Nice overview of programming concepts.', 2, 1),
    ('I found the database management topic very informative.', 3, 2),
    ('SQL queries can be challenging but rewarding to learn.', 4, 2),
    ('Web development is an exciting field with endless possibilities.', 5, 3),
    ('Building responsive websites is a key skill for modern developers.', 6, 3),
    ('I enjoyed learning about data structures and their applications.', 7, 4),
    ('Algorithms can seem intimidating at first, but practice makes perfect.', 8, 4),
    ('Computer networks play a crucial role in our interconnected world.', 9, 5),
    ('The internet is a marvel of modern technology.', 10, 5),
    ('This helped me a lot!', 6, 6),
    ('Nice overview of agile!', 7, 7),
    ('Thanks for sharing.', 8, 8),
    ('Very useful information!', 9, 9),
    ('Looking forward to more tutorials!', 10, 10);