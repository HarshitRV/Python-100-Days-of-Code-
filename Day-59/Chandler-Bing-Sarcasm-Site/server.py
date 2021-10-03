from flask import Flask, render_template, request, url_for
import requests
from send_mail import Mail, FormData
from sarcasm import Sarcasm

app = Flask(__name__)
app.config["SECRET_KEY"] = "somesecret"

@app.route("/")
def home():
    r = requests.get("https://sarcasm-api.herokuapp.com/sarcasm")
    data = r.json()

    return render_template("index.html", sarcasm=data, length=len(data))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<sno>")
def post(sno):
    r = requests.get("https://sarcasm-api.herokuapp.com/sarcasm")
    data = r.json()
    sarcasm = Sarcasm(sno=int(sno), comment=data[int(sno)]['sarcasm'])

    return render_template("post.html", comment=sarcasm)


@app.route("/contact", methods=["GET", "POST"])
def contact_default(default="Contact Me"):
    form = FormData()
    if form.validate_on_submit():
        return f"Passed info are : name={form.name.data}, email={form.email.data},\
                 phone={form.phone.data}, message={form.message.data}"
    
    return render_template("contact.html", default=default, form=form)

if __name__ == "__main__":
    app.run(debug=True)