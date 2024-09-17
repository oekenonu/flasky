from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Shouting from hello.py</h1>"

@app.route("/about")
def about():
    return "<h1>About Us</h1>"
