from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "super_secret_key_change_this"
DATABASE = "database.db"


# ---------------- DB CONNECTION ----------------
def get_db():
    return sqlite3.connect(DATABASE)


# ---------------- LOGIN REQUIRED DECORATOR ----------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first", "warning")
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = get_db()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            conn.commit()
            flash("Registration successful. Please login.", "success")
            return redirect("/login")

        except:
            flash("Username already exists", "danger")

        finally:
            conn.close()

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            flash("Login successful", "success")
            return redirect("/dashboard")

        flash("Invalid username or password", "danger")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
@login_required
def dashboard():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE user_id = ?",
        (session["user_id"],)
    )

    tasks = cursor.fetchall()
    conn.close()

    return render_template("dashboard.html", tasks=tasks)


# ---------------- ADD TASK ----------------
@app.route("/add-task", methods=["GET", "POST"])
@login_required
def add_task():
    if request.method == "POST":
        title = request.form["title"]

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tasks (title, user_id) VALUES (?, ?)",
            (title, session["user_id"])
        )

        conn.commit()
        conn.close()

        flash("Task added successfully", "success")
        return redirect("/dashboard")

    return render_template("add_task.html")


# ---------------- DELETE TASK ----------------
@app.route("/delete-task/<int:task_id>")
@login_required
def delete_task(t_
