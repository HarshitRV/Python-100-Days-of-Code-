from  flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import InputRequired

class AddBook(FlaskForm):
    book_name = StringField(label="Book Name", validators=[InputRequired()])
    book_author = StringField(label="Book Author", validators=[InputRequired()])
    rate = IntegerField(label="Rating", validators=[InputRequired()])
    add_book = SubmitField(label="Add Book")
