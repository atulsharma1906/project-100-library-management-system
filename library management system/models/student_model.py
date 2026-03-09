from db import db

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    stu_name = db.Column(db.String(100), nullable=False)
    stu_age = db.Column(db.Integer, nullable=False)
    stu_gender = db.Column(db.String(20))
    stu_course = db.Column(db.String(100))

    stu_email = db.Column(db.String(100), unique=True)
    stu_phone = db.Column(db.String(10), nullable=False, unique=True)

    stu_library_id = db.Column(db.String(50), unique=True)
    stu_join_date = db.Column(db.Date)

    stu_address = db.Column(db.Text)