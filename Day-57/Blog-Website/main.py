from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    r = requests.get("https://pacific-garden-82759.herokuapp.com/sarcasm")
    data = r.json()
    return render_template("index.html", sarcasm=data, length=len(data))

@app.route('/sarcasm/<sno>')
def get_sarcasm(sno):
    r = requests.get("https://pacific-garden-82759.herokuapp.com/sarcasm")
    data = r.json()
    post = Post(sno, data[int(sno)]["sarcasm"])
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
