# tutorial from https://pythonbasics.org/flask-tutorial-hello-world/

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World! This is my first Render.com deployment!"


