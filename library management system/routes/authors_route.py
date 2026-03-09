from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.author_model import Author
from db import db

author_bp = Blueprint("author", __name__, url_prefix="/author")


# -------------------------------
# Register Author
# -------------------------------
@author_bp.route("/author-register", methods=["GET", "POST"])
def author_register():

    if request.method == "POST":

        new_author = Author(
            auth_name=request.form.get("auth_name"),
            auth_email=request.form.get("auth_email"),
            auth_phone=request.form.get("auth_phone"),
            auth_country=request.form.get("auth_country"),
            auth_bio=request.form.get("auth_bio")
        )

        db.session.add(new_author)
        db.session.commit()

        flash("Author added successfully!", "success")

        return redirect(url_for("author.all_authors"))

    return render_template("author/author-register.html")


# -------------------------------
# Show All Authors
# -------------------------------
@author_bp.route("/authors")
def all_authors():

    authors = Author.query.all()

    return render_template(
        "author/all-authors.html",
        authors=authors
    )


# -------------------------------
# Author Details
# -------------------------------
@author_bp.route("/author-details/<int:id>")
def author_details(id):

    author = Author.query.get_or_404(id)

    return render_template(
        "author/author-details.html",
        author=author
    )


# -------------------------------
# Edit Author
# -------------------------------
@author_bp.route("/edit-author/<int:id>", methods=["GET","POST"])
def edit_author(id):

    author = Author.query.get_or_404(id)

    if request.method == "POST":

        author.auth_name = request.form.get("auth_name")
        author.auth_email = request.form.get("auth_email")
        author.auth_phone = request.form.get("auth_phone")
        author.auth_country = request.form.get("auth_country")
        author.auth_bio = request.form.get("auth_bio")

        db.session.commit()

        flash("Author updated successfully!", "success")

        return redirect(url_for("author.all_authors"))

    return render_template(
        "author/edit-author.html",
        author=author
    )


# -------------------------------
# Delete Author
# -------------------------------
@author_bp.route("/delete-author/<int:id>")
def delete_author(id):

    author = Author.query.get_or_404(id)

    db.session.delete(author)
    db.session.commit()

    flash("Author deleted successfully!", "danger")

    return redirect(url_for("author.all_authors"))