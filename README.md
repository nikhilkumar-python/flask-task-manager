# Flask Task Manager

## Live Demo

🚀 https://flask-task-manager-a50e.onrender.com

A simple **Task Management Web Application** built using **Python Flask**.
Users can **register, login, and manage their own tasks**.

---

## Features

* User Registration and Login
* Secure Password Hashing
* Add Tasks
* Edit Tasks
* Delete Tasks
* Mark Tasks as Completed
* User-specific tasks (each user sees only their tasks)
* REST API endpoints
* Bootstrap UI

---

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite
* Bootstrap

---

## Project Structure

```
flask-task-manager
│
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   └── templates
│
├── config.py
├── create_db.py
├── run.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/nikhilkumar-python/flask-task-manager.git
```

Go to the project directory:

```
cd flask-task-manager
```

Create virtual environment:

```
python -m venv venv
```

Activate virtual environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Create the database:

```
python create_db.py
```

Run the application:

```
python run.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## API Endpoints

Get all tasks:

```
GET /api/tasks
```

Create a task:

```
POST /api/tasks
```

Update a task:

```
PUT /api/tasks/<id>
```

Delete a task:

```
DELETE /api/tasks/<id>
```

---

## Author

**Nikhil Kumar**

GitHub:
https://github.com/nikhilkumar-python
