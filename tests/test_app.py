import pytest 
from app import app

# issues - change the structure of database -- it will still run correctly 
# drop everything, run the schema.sql file, run the insert sql file
# calls the database components to make sure it works


def test_index_page(test_app):
    response = test_app.get('/')
    
    data = response.data.decode('utf-8')
    
    assert response.status_code == 200


# validation error
def test_create_room_validation_error(test_app):
    response = test_app.post('/room')
    assert response.status_code == 400

# testing if the user enters optional text for creating their room
# change to description 
def test_create_room_optional(test_app):
    response = test_app.post('/room', data={
        'room_text':'room_text'
    })
    
    data = response.data.decode('utf-8')
    assert response.status_code == 400
    # call index there's no room already created
    # might have to delete if there's a creation 

# test if room is successfully created -- was the room actually created ? 



# getting rooms page when there's nothing
def test_get_rooms_empty(test_app):
    response = test_app.get('/room')
    
    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert '<h2>No rooms</h2>' in data

