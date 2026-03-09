from flask import *
book_bp=Blueprint("book",__name__)

@book_bp.route("/book-register")
def book_register():
    return render_template("book/book-register.html")