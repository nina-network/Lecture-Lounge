from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

def validate_signup_form(email, username, password, confirm_password):
    errors = []

    if not email.endswith('@uncc.edu') and not email.endswith('@charlotte.edu'):
        errors.append('Email must be from uncc.edu or charlotte.edu domain')

    if not username:
        errors.append('Please enter a username')

    if not password:
        errors.append('Please enter a password')

    if password != confirm_password:
        errors.append('Passwords do not match')

    return errors

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == 'your_username' and password == 'your_password':
            return redirect(url_for('profile_page'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        errors = validate_signup_form(email, username, password, confirm_password)

        if errors:
            return render_template('signup.html', error=errors[0])
        else:
            return redirect(url_for('login_page'))

    return render_template('signup.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')

@app.get('/room')
def room():
	return render_template('room.html')

@app.get('/createroom')
def create_room():
    return render_template('create_room.html')

@app.route('/search')
def search_page():
    return render_template('search.html')