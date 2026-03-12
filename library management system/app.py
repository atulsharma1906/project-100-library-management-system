from flask import *
from routes.students_route import student_bp

from routes.books_route import book_bp
from routes.authors_route import author_bp
from db import *
from config import Config
from flask_migrate import Migrate
from models import *
from sqlalchemy import text




app = Flask(__name__)

app.secret_key = "library_secret_key"

app.config.from_object(Config)
db.init_app(app)
migrate=Migrate(app,db)

@app.route("/db-health")
def db_health():
    try:
        db.session.execute(text("SELECT 1"))
        return{"status":"ok","database":"Connected"}
    except Exception as e:
        return {"status":str(e)}
    
# Login page will open first
from flask import render_template, request, redirect, session
from models.student_model import Student
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        student = Student.query.filter_by(stu_email=email).first()

        if student and bcrypt.check_password_hash(student.stu_pass, password):

            session["student_id"] = student.id
            session["student_name"] = student.stu_name

            return redirect(url_for("home"))

        else:
            return "Invalid Email or Password"

    return render_template("login.html")

@app.route("/")
def home():

    if "student_id" not in session:
        return redirect(url_for("login"))

    return render_template("home.html")

app.register_blueprint(student_bp,url_prefix="/student")
app.register_blueprint(book_bp,url_prefix="/book")  
app.register_blueprint(author_bp,url_prefix="/author")  

if __name__ == "__main__":
    app.run(debug=True)