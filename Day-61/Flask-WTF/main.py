from flask import Flask, render_template
from login import LoginForm

app =  Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"

@app.route("/form", methods=["GET", "POST"])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return "Passed data is : Username: {}. Password: {}".format(form.username.data, form.password.data)
    return render_template("form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)