from flask_wtf import FlaskForm
from wtforms import StringField

class Login(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')

