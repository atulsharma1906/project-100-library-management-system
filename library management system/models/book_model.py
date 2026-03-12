from db import db

class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(200), nullable=False)
    author_name = db.Column(db.String(100))
    isbn = db.Column(db.String(50))
    publisher = db.Column(db.String(100))
    year = db.Column(db.Integer)
    category = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    language = db.Column(db.String(50))
    description = db.Column(db.Text)