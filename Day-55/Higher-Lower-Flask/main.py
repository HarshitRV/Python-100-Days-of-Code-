from flask import Flask
import random

app = Flask(__name__)

random_num = 0

@app.route("/")
def home():
    global random_num
    random_num = random.randint(0,9)
    return "<h1 style='text-align:center;color:#FF00E4;'>Guess the number between 0 and 9</h1>"\
           "<img style='display:block;margin:0 auto;' src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='gif countdown'>"\

@app.route("/<int:number>")
def guess(number):
    if number == random_num:
        return  "<h1 style='text-align:center;color:#ED50F1;'>BANG ON RIGHT</h1>"\
                "<img style='display:block;margin:0 auto;' src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='gif correct'>"\
                "<h3 style='text-align:center;color:#FF00E4;font-size:50px;margin-bottom:0;'><a href='http://127.0.0.1:5000/'>🏡</a></h3>"\
                "<h3 style='text-align:center;color:#FF00E4;text-decoration:none;'><a href='http://127.0.0.1:5000/'>Go to Home for new number</a></h3>"


    elif number < random_num:
        return "<h1 style='text-align:center;color:#FDB9FC;'>Too Low</h1>"\
               "<img style='display:block;margin:0 auto;' src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='gif correct'>"\
               "<h3 style='text-align:center;color:#FF00E4;font-size:50px;margin-bottom:0;'><a href='http://127.0.0.1:5000/'>🏡</a></h3>"\
               "<h3 style='text-align:center;color:#FF00E4;text-decoration:none;'><a href='http://127.0.0.1:5000/'>Go to Home for new number</a></h3>"
               
    else:
        return "<h1 style='text-align:center;color:#FF0000;'>Too High</h1>"\
               "<img style='display:block;margin:0 auto;' src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='gif correct'>"\
               "<h3 style='text-align:center;color:#FF00E4;font-size:50px;margin-bottom:0;'><a href='http://127.0.0.1:5000/'>🏡</a></h3>"\
               "<h3 style='text-align:center;color:#FF00E4;text-decoration:none;'><a href='http://127.0.0.1:5000/'>Go to Home for new number</a></h3>"\


if __name__ == "__main__":
    app.run(debug=True)