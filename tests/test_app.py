import pytest 
from app import app

def test_index_page(test_app):
    response = test_app.get('/')
    
    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    # does a form show up ?? not much to test here.


# validation error
def test_create_room_validation_error(test_app):
    response = test_app.post('/room')
    assert response.status_code == 400

# testing if the user enters optional text for creating their room
def test_create_room_optional(test_app):
    response = test_app.post('/room', data={
        'room_text':'room_text'
    })
    data = response.data.decode('utf-8')
    assert response.status_code == 400


# getting rooms page when there's nothing
def test_get_rooms_empty(test_app):
    response = test_app.get('/room')
    
    data = response.data.decode('utf-8')
    
    # print("Response Data:", data)  [just debugging. will need later]
    
    assert response.status_code == 200
    assert '<h2>No rooms</h2>' in data

