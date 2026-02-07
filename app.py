from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-key-change-in-production")

# Security configurations
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = 3600  # 1 hour

DATABASE = os.path.join(os.path.dirname(__file__), "database.db")


# -------------------- DB CONNECTION --------------------
def get_db():
    """Get database connection with row factory"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# -------------------- LOGIN REQUIRED DECORATOR --------------------
def login_required(f):
    """Decorator to require login for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first", "warning")
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# -------------------- REGISTER --------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    """User registration route"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        confirm_password = request.form.get("confirm_password", "").strip()

        # Input validation
        if not username or not password:
            flash("Username and password are required", "danger")
            return render_template("register.html")

        if len(username) < 3:
            flash("Username must be at least 3 characters long", "danger")
            return render_template("register.html")

        if len(password) < 6:
            flash("Password must be at least 6 characters long", "danger")
            return render_template("register.html")

        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return render_template("register.html")

        hashed_password = generate_password_hash(password)

        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)\",
                (username, hashed_password)
            )
            conn.commit()
            conn.close()
            flash("Registration successful. Please login.", "success")
            return redirect("/login")

        except sqlite3.IntegrityError:
            flash("Username already exists", "danger")
        except Exception as e:
            flash("An error occurred during registration. Please try again.", "danger")
        finally:
            if conn:
                conn.close()

    return render_template("register.html")


# -------------------- LOGIN --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    """User login route"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            flash("Username and password are required", "danger")
            return render_template("login.html")

        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            conn.close()

            if user and check_password_hash(user["password"], password):
                session.permanent = True
                session["user_id"] = user["id"]
                session["username"] = user["username"]
                flash("Login successful", "success")
                return redirect("/dashboard")

            flash("Invalid username or password", "danger")

        except Exception as e:
            flash("An error occurred during login. Please try again.", "danger")

    return render_template("login.html")


# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    """User logout route"""
    session.clear()
    flash("You have been logged out", "success")
    return redirect("/login")


# -------------------- DASHBOARD --------------------
@app.route("/dashboard")
@login_required
def dashboard():
    """Display user tasks"""
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE user_id = ? ORDER BY created_at DESC\",
            (session["user_id"],)
        )
        tasks = cursor.fetchall()
        conn.close()

        return render_template("dashboard.html", tasks=tasks)

    except Exception as e:
        flash("An error occurred while loading tasks", "danger")
        return redirect("/dashboard")


# -------------------- ADD TASK --------------------
@app.route("/add-task", methods=["GET", "POST"])
@login_required
def add_task():
    """Add a new task"""
    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if not title:
            flash("Task title is required", "danger")
            return render_template("add_task.html")

        if len(title) > 200:
            flash("Task title must be less than 200 characters", "danger")
            return render_template("add_task.html")

        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks (title, user_id) VALUES (?, ?)\",
                (title, session["user_id"])
            )
            conn.commit()
            conn.close()

            flash("Task added successfully", "success")
            return redirect("/dashboard")

        except Exception as e:
            flash("An error occurred while adding the task", "danger")

    return render_template("add_task.html")


# -------------------- DELETE TASK --------------------
@app.route("/delete-task/<int:task_id>")
@login_required
def delete_task(task_id):
    """Delete a task"""
    try:
        conn = get_db()
        cursor = conn.cursor()

        # Verify the task belongs to the current user
        cursor.execute(
            "SELECT user_id FROM tasks WHERE id = ?",
            (task_id,)
        )
        task = cursor.fetchone()

        if not task or task["user_id"] != session["user_id"]:
            flash("Task not found or you do not have permission to delete it", "danger")
            conn.close()
            return redirect("/dashboard")

        # Delete the task
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

        flash("Task deleted successfully", "success")

    except Exception as e:
        flash("An error occurred while deleting the task", "danger")

    return redirect("/dashboard")


# -------------------- ROOT ROUTE --------------------
@app.route("/")
def index():
    """Redirect to dashboard if logged in, otherwise to login"""
    if "user_id" in session:
        return redirect("/dashboard")
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)