import flask

app = flask.Flask(__name__)
from app import app

@app.route('/')
def index():
    return "Hello, world!"