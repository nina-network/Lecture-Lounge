from flask import Flask, render_template, urlfor, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')

@app.get('/room')
def room():
	return render_template('room.html', room = room)