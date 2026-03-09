from flask import *
from routes.students_route import student_bp
from routes.books_route import *
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

@app.route("/")
def home():
    return render_template("home.html")

app.register_blueprint(student_bp,url_prefix="/student")
app.register_blueprint(book_bp,url_prefix="/book")  
app.register_blueprint(author_bp,url_prefix="/author")  

if __name__ == "__main__":
    app.run(debug=True)