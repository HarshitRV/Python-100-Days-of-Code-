from os import name
from urllib.parse import uses_relative
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.exceptions import RequestTimeout
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask import session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            name = request.form.get("name"),
            email = request.form.get("email"),
            password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        )
        # try to save user info in DB
        try:
            db.session.add(new_user)
            db.session.commit()
        # an exception will be raised if user already exists
        except sqlalchemy.exc.IntegrityError:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        login_user(new_user)
        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        # find user as per email in DB
        user = User.query.filter_by(email=email).first()

        # if user found
        if user:
            # if user exists check password
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("secrets"))
            # if password entered is wrong flash the message
            else:
                flash('Password incorrect, please try again.')
                return redirect(url_for('login'))
        # if user does not exists
        else:
            flash("That email does not exist, please register.")
            return redirect(url_for('register'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download', methods=["GET", "POST"])
@login_required
def download():
    return send_from_directory(
        directory='static/files', 
        path=request.args.get("filename"), 
        as_attachment=True
    )

@app.route("/delete")
def delete():
    for i in range(1,18):
        to_delete = User.query.get(i)
        db.session.delete(to_delete)
        db.session.commit()
    return "Delted every one from DB"


if __name__ == "__main__":
    app.run(debug=True)
