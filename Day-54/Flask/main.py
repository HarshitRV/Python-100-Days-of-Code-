from re import L
from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye see you soon!"

if __name__ == "__main__":
    app.run()