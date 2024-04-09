from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

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

    # Render login page for GET request
    return render_template('login.html')

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