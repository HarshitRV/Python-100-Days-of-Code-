from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrap_function():
        return f"<h1><b>{function()}</b></h1>"
    return wrap_function

@app.route("/")
@bold
def say_hi():
    return "Hello"

@app.route("/user/<name>")
def greet(name):
    return f"Hello there {name}"

if __name__ == "__main__":
    app.run(debug=True)