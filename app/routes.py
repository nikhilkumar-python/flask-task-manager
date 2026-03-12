from flask import Blueprint, render_template, request, redirect
from app.models import Task
from app import db
from flask import jsonify
from flask_login import login_required, current_user

main = Blueprint("main", __name__)

@main.route("/")
@login_required
def index():

    tasks = Task.query.filter_by(user_id=current_user.id).all()

    return render_template("index.html", tasks=tasks)

@main.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title")

    new_task = Task(title=title, user_id=current_user.id)

    db.session.add(new_task)

    db.session.commit()

    return redirect("/")

@main.route("/delete/<int:id>")
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    return redirect("/")

@main.route("/complete/<int:id>")
def complete_task(id):

    task = Task.query.get_or_404(id)

    task.completed = True

    db.session.commit()

    return redirect("/")

@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):

    task = Task.query.get_or_404(id)

    if request.method == "POST":

        task.title = request.form["title"]

        db.session.commit()

        return redirect("/")

    return render_template("edit.html", task=task)

@main.route("/api/tasks", methods=["GET"])
def get_tasks():

    tasks = Task.query.all()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        })

    return jsonify(task_list)

@main.route("/api/tasks", methods=["POST"])
def create_task():

    data = request.json

    new_task = Task(title=data["title"])

    db.session.add(new_task)

    db.session.commit()

    return jsonify({"message": "Task created"})

@main.route("/api/tasks/<int:id>", methods=["PUT"])
def update_task(id):

    task = Task.query.get_or_404(id)

    data = request.json

    task.title = data["title"]

    task.completed = data["completed"]

    db.session.commit()

    return jsonify({"message": "Task updated"})

@main.route("/api/tasks/<int:id>", methods=["DELETE"])
def delete_task_api(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    return jsonify({"message": "Task deleted"})
