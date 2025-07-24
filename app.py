from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Yo guys, this is my flask app!"
