from flask import Flask, render_template, urlfor, request, redirect

app = Flask(__name__)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')