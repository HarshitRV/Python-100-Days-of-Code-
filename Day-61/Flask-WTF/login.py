from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField #fields
from wtforms.validators import InputRequired  #validators

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[InputRequired])
    password = PasswordField(label='Password')
    submit = SubmitField(label='Submit')
