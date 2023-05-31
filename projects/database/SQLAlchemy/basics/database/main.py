# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# DB SETUP
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# CREATE DB
db = SQLAlchemy(app)

# CREATE TABLE


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
    

with app.app_context():
    db.create_all()

    # CREATE RECORD
    new_book = Book(id=1, title="harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()


    # READ ALL RECORDS
    all_books = db.session.query(Book).all()
    print(all_books)

    # READ A SINGLE RECORD
    book = db.session.query(Book).filter_by(title="Potter").first()
    print(type(book))

    # UPDATE A PARTICULAR RECORD BY QUERY
    book_to_update = db.session.execute(db.select(Book).filter_by(title="harry Potter"))
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()


    # UPDATE A PARTICULAR RECORD BY PRIMARY KEY
    book_id = 1
    book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

    # DELETE A PARTICULAR RECORD BY PRIMARY KEY
    book_id = 1
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
