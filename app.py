from flask import Flask, rendertemplate, urlfor, request, redirect

app = Flask(__name__)

@app.get('/room')
def room():
	return rendertemplate('room.html', room = room)
