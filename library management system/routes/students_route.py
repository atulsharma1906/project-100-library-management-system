from flask import Blueprint, render_template, request, redirect, url_for
from models.student_model import Student
from db import db

student_bp = Blueprint('student', __name__)


# Register Student
@student_bp.route('/student-register', methods=['GET', 'POST'])
def register_student():

    if request.method == "POST":

        new_student = Student(
            stu_name=request.form.get("student_name"),
            stu_age=request.form.get("age"),
            stu_gender=request.form.get("gender"),
            stu_course=request.form.get("course"),
            stu_email=request.form.get("email"),
            stu_phone=request.form.get("phone"),
            stu_library_id=request.form.get("library_id"),
            stu_join_date=request.form.get("join_date"),
            stu_address=request.form.get("address")
        )

        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for("student.all_students"))

    return render_template("students/register-student.html")


# Show All Students
@student_bp.route('/students')
def all_students():

    students = Student.query.all()

    return render_template("students/all-students.html", students=students)


# Student Details
@student_bp.route('/student-details/<int:id>')
def students_details(id):

    student = Student.query.get_or_404(id)

    return render_template("students/students-details.html", student=student)


# Delete Student
@student_bp.route('/delete-student/<int:id>')
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for("student.all_students"))


# Edit Student
@student_bp.route('/edit-student/<int:id>', methods=['GET','POST'])
def edit_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student.stu_name = request.form.get("student_name")
        student.stu_age = request.form.get("age")
        student.stu_gender = request.form.get("gender")
        student.stu_course = request.form.get("course")
        student.stu_email = request.form.get("email")
        student.stu_phone = request.form.get("phone")
        student.stu_library_id = request.form.get("library_id")
        student.stu_join_date = request.form.get("join_date")
        student.stu_address = request.form.get("address")

        db.session.commit()

        return redirect(url_for("student.all_students"))

    return render_template("students/edit-student.html", student=student)