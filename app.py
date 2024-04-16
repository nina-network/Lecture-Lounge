from flask import Flask, render_template, url_for, request, redirect, abort
from random import randint

app = Flask(__name__)

rooms = {}
room_texts = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    return render_template('signup.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')

@app.get('/room')
def room():
	return render_template('room.html', rooms=rooms, room_texts=room_texts)


# name and text -- reconfigure after database is integrated
@app.post('/room')
def create_rooms():
    room_name = request.form.get('room_name')
    room_text = request.form.get('room_text')
    if not room_name:
        abort(400)
    room_id = randint(1,1000)
    rooms[room_id] = room_name
    room_texts[room_id] = room_text
    return redirect('/room')

@app.get('/createroom')
def create_room():
    return render_template('create_room.html')

@app.route('/search')
def search_page():
    return render_template('search.html')