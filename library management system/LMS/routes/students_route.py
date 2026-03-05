from flask import *
student_bp=Blueprint("student",__name__)

@student_bp.route("/student-register")
def student_register():
    return "register here for student "