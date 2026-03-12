from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user
from app.models import User
from app import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User(username=username)

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):

            login_user(user)

            return redirect("/")

    return render_template("login.html")

@auth.route("/logout")
def logout():

    logout_user()

    return redirect("/login")