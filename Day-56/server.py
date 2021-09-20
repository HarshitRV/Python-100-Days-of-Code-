from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/work")
def work():
    return render_template("work.html")

if __name__ == "__main__":
    app.run(debug=True)

