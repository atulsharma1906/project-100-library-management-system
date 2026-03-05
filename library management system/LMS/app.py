from flask import *
from routes.students_route import *
from routes.books_route import *
from routes.authors_route import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

app.register_blueprint(student_bp,url_prefix="/student")
app.register_blueprint(book_bp,url_prefix="/book")  
app.register_blueprint(author_bp,url_prefix="/author")  


app.run(debug=True)