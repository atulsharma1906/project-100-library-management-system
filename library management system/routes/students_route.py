from flask import Blueprint, render_template, request
from models.student_model import Student
from db import db

student_bp = Blueprint('student', __name__)

@student_bp.route('/student-register', methods=['GET', 'POST'])
def register_student():

    if request.method == "POST":

        name = request.form.get("student_name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        course = request.form.get("course")
        email = request.form.get("email")
        phone = request.form.get("phone")
        library_id = request.form.get("library_id")
        join_date = request.form.get("join_date")
        address = request.form.get("address")

        new_student = Student(
            stu_name=name,
            stu_age=age,
            stu_gender=gender,
            stu_course=course,
            stu_email=email,
            stu_phone=phone,
            stu_library_id=library_id,
            stu_join_date=join_date,
            stu_address=address
        )

        db.session.add(new_student)
        db.session.commit()

        print("Student saved successfully")

    return render_template("students/register-student.html")

@student_bp.route('/students')
def all_students():

    students = Student.query.all()

    return render_template("students/all-students.html", students=students)

@student_bp.route('/student-details/<int:id>')
def students_details(id):

    student = Student.query.get(id)

    return render_template("students/students-details.html",student=student)