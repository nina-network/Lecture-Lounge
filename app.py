import os
from flask import Flask, render_template, session, url_for, request, redirect, abort
from authlib.integrations.flask_client import OAuth
from repositories import course_repository, post_repository
from random import randint
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

from repositories import user_repository

load_dotenv()

app = Flask(__name__)

bcrypt = Bcrypt(app)

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

@app.get('/')
def index():

    # query the database for all courses and posts
    courses = course_repository.get_all_courses();
    posts = post_repository.get_all_posts();

    if not courses or not posts:
        abort(400)

    room_posts = {}

    # sort posts by course
    for course in courses:
        counter = 0
        room_posts[course['course_id']] = []
        for post in posts:
            if course['course_id'] == post['course_id'] and counter < 3:
                room_posts[course['course_id']].append(post)
                counter += 1
    
    # map course_id to course_name
    course_names = {}
    for course in courses:
        course_names[course['course_id']] = course['course_name']

    return render_template('index.html', posts=room_posts, courses=course_names)

@app.get('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        abort(400)
    user = user_repository.get_user_by_username(username)
    if user is None:
        abort(401)
    if not bcrypt.check_password_hash(user['hashed_password'], password):
        abort(401)
    session['user'] = user
    return redirect(url_for('index'))

# Google login
@app.get('/google-login')
def googleLogin():
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("googleCallback", _external=True))

# callback for Google login
@app.get('/signin-google')
def googleCallback():
    token = oauth.myApp.authorize_access_token() # authorize and store token
    session['user'] = token # store token in session, indicating user is logged in
    return redirect(url_for('profile_page'))

# logout
@app.get('/logout')
def logout():
    session.pop('user', None) # remove token from session (log out user)
    return redirect(url_for('login_page'))

@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    role = request.form.get('role')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if not all([first_name, last_name, email, role, username, password, confirm_password]):
        error = "All fields are required."
        return render_template('signup.html', error=error)
    
    if user_repository.get_user_by_email(email):
        error = "Email is already registered."
        return render_template('signup.html', error=error)

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user_repository.create_user(first_name, last_name, email, role, username, hashed_password)

    return redirect(url_for('login_page'))

@app.get('/profile')
def profile_page():
    return render_template('profile.html')

@app.get('/room/<room_id>')
def room(room_id):
    room = course_repository.get_course_by_id(room_id)
    if not room:
        abort(400)
    return render_template('room.html', room=room)

# name and text -- reconfigure after database is integrated
@app.post('/room')
def create_rooms():
    course_name = request.form.get('course_name')
    description = request.form.get('description')
    
    if not course_name:
        abort(400)
    
    new_course = {'course_name': course_name, 'description': description}
    course_repository.create_course(new_course) 

    room_courses = {}
    for course in course_repository.get_all_courses():
        if course['course_id'] not in room_courses:
            room_courses[course['course_id']] = []
        room_courses[course['course_id']].append(course)
        room_courses[course['course_id']] = room_courses[course['course_id']][:3]
    
    return redirect(url_for('index', room_courses=room_courses))


@app.get('/createroom')
def create_room():
    return render_template('create_room.html')

@app.route('/search')
def search_page():
    return render_template('search.html')