from flask import Flask, render_template, session, url_for, request, redirect, abort
from authlib.integrations.flask_client import OAuth
from random import randint
from dotenv import load_dotenv
import os

load_dotenv() 

app = Flask(__name__)

# Configuration with OAuth2 client ID and secret
appConf = {
    "OAUTH2_CLIENT_ID": os.getenv("OAUTH2_CLIENT_ID"),
    "OAUTH2_CLIENT_SECRET": os.getenv("OAUTH2_CLIENT_SECRET"),
    "OAUTH2_META_URL": "https://accounts.google.com/.well-known/openid-configuration",
    "FLASK_SECRET": "ffkj64qu3RKR3giJxwE5vcTXNN4JMBNV",
    "FLASK_PORT": 5000
}

app.secret_key = appConf["FLASK_SECRET"]

#Oauth app
oauth = OAuth(app)

# register the app with the OAuth provider with the name 'myApp'
oauth.register("myApp",
                client_id=appConf["OAUTH2_CLIENT_ID"],
                client_secret=appConf["OAUTH2_CLIENT_SECRET"],
                server_metadata_url=appConf["OAUTH2_META_URL"],
                client_kwargs={"scope": "openid profile email"}
               )

rooms = {}
room_texts = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

# Google login
@app.route('/google-login')
def googleLogin():
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("googleCallback", _external=True))

# callback for Google login
@app.route('/signin-google')
def googleCallback():
    token = oauth.myApp.authorize_access_token() # authorize and store token
    session['user'] = token # store token in session, indicating user is logged in
    return redirect(url_for('profile_page'))

# logout
@app.route('/logout')
def logout():
    session.pop('user', None) # remove token from session (log out user)
    return redirect(url_for('login_page'))

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