from flask import Flask, render_template
from datetime import date
import requests
from werkzeug.wrappers import response

today = date.today()

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("https://pacific-garden-82759.herokuapp.com/sarcasm")
    sarcasm_data = response.json()

    return render_template("index.html", year=today.year, sarcasm=sarcasm_data)

@app.route("/guess/<name>")
def guess(name):
    response_age = requests.get(f"https://api.agify.io/?name={name}")
    data_age = response_age.json()

    response_gender = requests.get(f"https://api.genderize.io/?name={name}")
    data_gender = response_gender.json()

    return render_template("guess.html", age=data_age["age"], gender=data_gender["gender"])

@app.route("/blog/<num>")
def get_comment(num):
    print(num)
    r = requests.get("https://pacific-garden-82759.herokuapp.com/sarcasm")
    data = r.json()
    return render_template("sarcasm.html", sarcasm=data)

if __name__ == "__main__":
    app.run(debug=True)