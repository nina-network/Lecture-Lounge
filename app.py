import os, re
from flask import Flask, render_template, session, url_for, request, redirect, abort, jsonify
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

email_regex = r'^[a-zA-Z0-9._%+-]+@uncc\.edu$'
password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{12,}$'

@app.get('/')
def index():

    # query the database for all courses and posts
    try:
        courses = course_repository.get_all_courses();
        posts = post_repository.get_all_posts();
    except:
        # render error page here
        return "<h1>Error Occurred</h1>" # temporary error

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
    email = token['userinfo']['email']

    # check if email is uncc.edu email, redirect to login page and display error message if not
    if not re.match(email_regex, email):
        error = "Please use a valid @uncc.edu email address."
        return render_template('login.html', error=error)
    
    session['first_name'] = token['userinfo']['given_name']
    session['last_name'] = token['userinfo']['family_name']
    session['email'] = email

    print(token)
    # check if email is in DB
    # if not in DB, redirect to sign up page where user can enter username and role
    user = user_repository.get_user_by_email(email)
    if user is None:
        return redirect(url_for('signup_auth'))
    # store token in session, indicating user is logged in
    session['user'] = token
    return redirect(url_for('profile_page'))

# logout
@app.get('/logout')
def logout():
    session.pop('user', None) # remove token from session (log out user)
    return redirect(url_for('login_page'))

@app.get('/signup-auth')
def signup_auth():
    return render_template("oauth_signup.html")

# POST REQUEST HERE FOR OAUTH
@app.post('/signup-auth')
def signup_auth_post():
    username = request.form.get('username')
    first_name = session['first_name']
    last_name = session['last_name']
    user_role = request.form.get('role').lower()
    email = session['email']

    if not username or not user_role:
        abort(400)

    if user_role == "ta":
        user_role = user_role.upper()

    user_repository.create_oauth_user(first_name, last_name, username, user_role, email)
    return redirect(url_for('profile_page'))

@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    role = request.form.get('role').lower()
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    
    valid_roles = ['student', 'TA', 'admin']
    if role not in valid_roles:
        error = f"Invalid role: {role}. Please choose from {', '.join(valid_roles)}."
        return render_template('signup.html', error=error)

    if not re.match(email_regex, email):
        error = "Please use a valid @uncc.edu email address."
        return render_template('signup.html', error=error)

    if not re.match(password_regex, password):
        error = "Password must contain at least 12 characters including uppercase, lowercase, number, and special character."
        return render_template('signup.html', error=error)

    if not all([first_name, last_name, email, role, username, password, confirm_password]):
        error = "All fields are required."
        return render_template('signup.html', error=error)

    if user_repository.get_user_by_email(email):
        error = "Email is already registered."
        return render_template('signup.html', error=error)
    
    if user_repository.get_user_by_username(username):
        error = "Username is already taken."
        return render_template('signup.html', error=error)
    
    if role == "ta":
        role = role.upper()

    if password != confirm_password:
        error = "Passwords do not match."
        return render_template('signup.html', error=error)

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user_repository.create_user(first_name, last_name, email, role, username, hashed_password)

    return redirect(url_for('login_page'))

@app.get('/profile')
def profile_page():
    if 'user' not in session:
        return redirect(url_for('login_page'))
    
    user_id = session['user'].get('user_id')
    profile_pic = user_repository.get_profile_picture(user_id)
    user_posts = post_repository.get_post_by_user_id(user_id)

    if profile_pic:
        profile_pic = profile_pic['user_pic']
        return render_template('profile.html', profile_pic=profile_pic, user_posts=user_posts, get_user_by_id=user_repository.get_user_by_id, get_course_name=course_repository.get_course_name_by_id)
    if 'picture' in session:
        user_id = user_repository.get_user_id_by_email(session['email'])
        user_id = user_id['user_id']
        profile_pic = session['picture']
        user_posts = post_repository.get_post_by_user_id(user_id)
        return render_template('profile.html', profile_pic=profile_pic, user_posts=user_posts, get_user_by_id=user_repository.get_user_by_id, get_course_name=course_repository.get_course_name_by_id)
    if 'email' in session:
        user_id = user_repository.get_user_id_by_email(session['email'])
        user_id = user_id['user_id']
        user_posts = post_repository.get_post_by_user_id(user_id)
        return render_template('profile.html', user_posts=user_posts, get_user_by_id=user_repository.get_user_by_id, get_course_name=course_repository.get_course_name_by_id)

    return render_template('profile.html', user_posts=user_posts, get_user_by_id=user_repository.get_user_by_id, get_course_name=course_repository.get_course_name_by_id)

pics = ['default_pic.jpg', 'prof_img1.jpg', 'prof_img2.jpg'
            , 'prof_img3.jpg', 'prof_img4.jpg', 'prof_img5.jpg'
            , 'prof_img6.jpg', 'prof_img7.jpg', 'prof_img8.jpg'
            , 'prof_img9.jpg', 'prof_img10.jpg', 'prof_img11.jpg']

@app.get('/profile-pic')
def profile_pic_page():
    if 'user' not in session:
        return redirect(url_for('login_page'))
    return render_template('profile_pic_page.html', pics=pics)

@app.post('/update-pic')
def set_profile_pic():
    if 'user' not in session:
        abort(400)
    profile_pic = request.form.get('profile_pic')
    if not profile_pic:
        abort(400)

    # for manual sign-in
    if(session['user'].get('user_id')):
        session['user']['profile_pic'] = profile_pic
        user_id = session['user']['user_id'] 
        user_repository.set_profile_picture(user_id, profile_pic)
    
    # for google sign-in
    session['picture'] = profile_pic
    user_id = user_repository.get_user_id_by_email(session['email'])
    user_repository.set_profile_picture(user_id['user_id'], profile_pic)
    
    return redirect(url_for('profile_page', profile_pic=profile_pic))

room_posts = {}

@app.get('/room/<room_id>')
def room(room_id):
    room = course_repository.get_course_by_id(room_id)
    if not room:
        abort(400)

    course_ids = course_repository.get_all_course_ids()

    for course_id in course_ids:
        room_posts[course_id] = post_repository.get_post_by_course_id(course_id)
    
    if 'user' not in session:
        return redirect(url_for('login_page'))
    
    return render_template('room.html', room=room, room_posts=room_posts, get_user_by_id=user_repository.get_user_by_id)

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

@app.post('/create-post')
def create_post():
    post_title = request.form.get('post_title')
    post_content = request.form.get('post_content')
    user_id = request.form.get('user_id')
    course_id = request.form.get('course_id')

    if not post_title or not post_content or not course_id:
        abort(400)

    if not user_id:
        user_id = user_repository.get_user_id_by_email(session['email'])
        user_id = user_id['user_id']

    new_post = {'title' : post_title,
                'content' : post_content,
                'user_id' : user_id,
                'course_id' : course_id}
    post_repository.create_new_post(new_post['title'], new_post['content'], new_post['user_id'], new_post['course_id'])

    for post in post_repository.get_all_posts():
        if post['course_id'] not in room_posts:
            room_posts[post['course_id']] = []
        room_posts[post['course_id']].append(post)
        room_posts[post['course_id']] = room_posts[post['course_id']]

    return redirect(url_for('room', room_id=course_id))

@app.route('/search', methods=['GET', 'POST'])
def search_page():
    message = None
    search_results = {}
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            courses = course_repository.get_all_courses()
            if not courses:
                abort(400)  
            for course in courses:
                if search_query.lower() in course['course_name'].lower():
                    search_results[course['course_id']] = course['course_name']
            if not search_results:
                message = "No rooms with that name were found."
    
    return render_template('search.html', search_results=search_results, message=message)

@app.route('/delete-post/<string:title>', methods=['POST'])
def delete_post(title):
    post_repository.delete_post_by_title(title)
    return jsonify({'success': True})