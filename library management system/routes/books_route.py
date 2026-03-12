from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.book_model import Book
from db import db

book_bp = Blueprint("book", __name__, url_prefix="/book")


# Register Book
@book_bp.route("/book-register", methods=["GET","POST"])
def book_register():

    if request.method == "POST":

        book = Book(
            book_title=request.form.get("book_title"),
            author_name=request.form.get("author_name"),
            isbn=request.form.get("isbn"),
            publisher=request.form.get("publisher"),
            year=request.form.get("year"),
            category=request.form.get("category"),
            quantity=request.form.get("quantity"),
            language=request.form.get("language"),
            description=request.form.get("description")
        )

        db.session.add(book)
        db.session.commit()

        flash("Book added successfully", "success")

        return redirect(url_for("book.all_book"))

    return render_template("book/book-register.html")


# Show All Books
@book_bp.route("/books")
def all_books():

    books = Book.query.all()

    return render_template(
        "book/all-books.html",
        books=books
    )


# Book Details
@book_bp.route("/book-details/<int:id>")
def book_details(id):

    book = Book.query.get_or_404(id)

    return render_template(
        "book/book-details.html",
        book=book
    )


# Edit Book
@book_bp.route("/edit-book/<int:id>", methods=["GET","POST"])
def edit_book(id):

    book = Book.query.get_or_404(id)

    if request.method == "POST":

        book.book_title = request.form.get("book_title")
        book.author_name = request.form.get("author_name")
        book.isbn = request.form.get("isbn")
        book.publisher = request.form.get("publisher")
        book.year = request.form.get("year")
        book.category = request.form.get("category")
        book.quantity = request.form.get("quantity")
        book.language = request.form.get("language")
        book.description = request.form.get("description")

        db.session.commit()

        flash("Book updated successfully", "success")

        return redirect(url_for("book.all_books"))

    return render_template(
        "book/edit-book.html",
        book=book
    )


# Delete Book
@book_bp.route("/delete-book/<int:id>")
def delete_book(id):

    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    flash("Book deleted successfully", "danger")

    return redirect(url_for("book.all_books"))