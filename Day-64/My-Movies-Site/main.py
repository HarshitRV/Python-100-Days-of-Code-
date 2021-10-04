from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from movie_form import RateMovieForm
from movies import MoviesInfo
import requests
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String(100), nullable=False)

db.create_all()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = RateMovieForm()
    to_edit = Movie.query.get(id)

    try:
        movie_data = MoviesInfo(
            title= to_edit.title,
            rating = to_edit.rating,
            ranking = to_edit.review
        )
    except AttributeError:
        return redirect(url_for('home'))


    if form.validate_on_submit():
        print(form.rating.data)
        print(form.review.data)
        print(type(form.rating.data))
        print(type(form.review.data))
        print(float(form.rating.data), type(float(form.rating.data)))
        
        to_edit.rating = float(form.rating.data)
        to_edit.review = form.review.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie_data=movie_data)

if __name__ == '__main__':
    app.run(debug=True)
