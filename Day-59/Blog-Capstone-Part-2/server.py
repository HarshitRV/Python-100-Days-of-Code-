from os import name
from flask import Flask, render_template, request, url_for
import requests
from werkzeug.utils import redirect
from send_mail import Mail

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get("https://pacific-garden-82759.herokuapp.com/sarcasm")
    data = r.json()

    return render_template("index.html", sarcasm=data, length=len(data))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/contact")
def contact_default(default="Contact Me"):
    return render_template("contact.html", default=default)

# FORM LOGIN

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.form

        mail = Mail(name=data['name'], sender_email=data['email'], phone=data['phone'], message=data['message'])
        mail.send_mail()

        return render_template("contact.html", default="Successfully sent your message!")
    return render_template("contact.html", default="Message could not be sent :(")
if __name__ == "__main__":
    app.run(debug=True)