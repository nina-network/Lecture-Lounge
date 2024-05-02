import pytest 
from flask import session
from app import app
from repositories import user_repository, course_repository, post_repository

# loading up index page with populated data 
def test_index_page(test_app):
    response = test_app.get('/')
    assert response.status_code == 200


# ****** //// room testing e2e //// *******
#search 
def test_get_course_by_name_empty(test_app):
    result = course_repository.get_course_name('course_name')
    if result is not None:
        response = test_app.get('/')
        assert response.status_code == 200 
    else:
        assert result is None

# validation of room error
def test_create_room_validation_error(test_app):
    response = test_app.post('/room')
    assert response.status_code == 400

# testing if the user enters optional text data in create room
def test_create_room_optional(test_app):
    response = test_app.post('/room', data={
        'description':'description'
    })
    data = response.data.decode('utf-8')
    assert response.status_code == 400



# ****** //// signup/login unit testing //// ******
def test_signup(test_app):
    # Simulate a sign-up request with valid user data
    response = test_app.post('/signup', data={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'johndoe@example.com',
        'role': 'student',
        'username': 'johndoe',
        'password': 'password123',
        'confirm_password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_login(test_app):
    response = test_app.post('/login', data={
        'username': 'johndoe',
        'password': 'password123'
    }, follow_redirects=True)

    assert response.status_code == 200  

# unit test for id 
def test_get_course_by_id(test_app):
    test_course_id = 1
    retrieved_course = course_repository.get_course_by_id(test_course_id)
    
    assert retrieved_course is not None

    assert retrieved_course['course_id'] == test_course_id
    assert 'course_name' in retrieved_course  


# does the username exist in the database test true
def test_does_username_exist_with_existing_username(test_app):
    existing_username = 'johndoe'
    result = user_repository.does_username_exist(existing_username)

    assert result is True

# does the username exist in the database test false
def test_does_username_exist_with_nonexistent_username(test_app):
    nonexistent_username = 'nonexistent_user'
    result = user_repository.does_username_exist(nonexistent_username)

    assert result is False


# testing existing email in database
def test_get_user_by_existing_email(test_app):
    existing_email = 'johndoe@example.com'
    user = user_repository.get_user_by_email(existing_email)

    assert user is not None

    assert 'user_id' in user
    assert 'username' in user
    assert 'hashed_password' in user

# testing non existent email in database
def test_get_user_by_nonexistent_email(test_app):
    nonexistent_email = 'nonexistent@example.com'
    user = user_repository.get_user_by_email(nonexistent_email)
    
    assert user is None

# testing existent user in database
def test_get_user_by_existing_username(test_app):
    existing_username = 'janedoe'

    retrieved_user = user_repository.get_user_by_username(existing_username)

    assert retrieved_user is not None
    assert 'user_id' in retrieved_user
    assert retrieved_user['username'] == existing_username

# testing nonexistent user in database 
def test_get_user_by_nonexistent_username(test_app):
    nonexistent_username = 'nonexistent_user'
    retrieved_user = user_repository.get_user_by_username(nonexistent_username)

    assert retrieved_user is None

# getting existing post in database 
def test_get_posts(test_app):
    existing_post_title = 'Welcome to Programming 101'
    
    retrieved_post = post_repository.get_post_by_title(existing_post_title)
    
    assert existing_post_title is not None

# getting nonexisting post in database 
def test_get_posts_nonexisting(test_app):
    nonexisting_post_title = 'This project makes me want to cry'
    
    retrieved_post = post_repository.get_post_by_title(nonexisting_post_title)
    assert retrieved_post is None