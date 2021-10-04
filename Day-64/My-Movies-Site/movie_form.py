from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

