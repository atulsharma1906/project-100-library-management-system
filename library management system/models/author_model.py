from db import db

class Author(db.Model):
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True)

    auth_name = db.Column(db.String(100), nullable=False)
    auth_email = db.Column(db.String(100), unique=True)
    auth_phone = db.Column(db.String(10), nullable=False, unique=True)

    auth_country = db.Column(db.String(50), nullable=False)
    auth_bio = db.Column(db.String(100))
    role=db.Column(db.String(20),nullable=False)