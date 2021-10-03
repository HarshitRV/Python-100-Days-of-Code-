from flask import Flask, render_template, redirect, url_for, request
from data import AddBook, EditRating
from flask_sqlalchemy import SQLAlchemy
from book import BookInfo

app = Flask(__name__)
app.config['SECRET_KEY'] = "iamasecret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///book-list.db"

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()

@app.route('/')
def home():
    books = db.session.query(Book).all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET","POST"])
def add():
    form = AddBook()
    if form.validate_on_submit():
        print("Submitted")
        new_book = Book(
            title = form.book_name.data,
            author = form.book_author.data,
            rating = form.rate.data
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template("add.html", form=form)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
   
    book_to_update = Book.query.get(id)

    try:
        book = BookInfo(
            book_name=book_to_update.title,
            book_rating=book_to_update.rating
        )
    except AttributeError:
        return "<h1>Not found<h1><a href='/'>HOME<a>"

    if request.method == 'POST':
        req = request.form

        # print(req['edit_rating'], type(req['edit_rating']))
        book_to_update.rating = float(req['edit_rating'])
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", book=book, id=id)

@app.route("/delete/<int:id>")
def delete(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)