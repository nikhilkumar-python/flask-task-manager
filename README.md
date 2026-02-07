# Flask Task Manager

<div align="center">

![Flask](https://img.shields.io/badge/Flask-2.0+-blue?style=for-the-badge&logo=flask)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A modern task management web application built with Flask that enables users to securely register, authenticate, and manage their daily tasks with an intuitive user interface.

[Features](#features) • [Installation](#installation--setup) • [Usage](#usage) • [Project-structure](#project-structure) • [API-endpoints](#api-endpoints) • [Contributing](#contributing)

</div>

---

## 📋 Overview

Flask Task Manager is a full-stack web application designed to help users organize and track their daily tasks efficiently. The application prioritizes security, maintainability, and user experience through modern Flask best practices and a modular architecture.

## ✨ Features

- **User Authentication** - Secure registration and login with password hashing
- **Task Management** - Create, read, update, and delete tasks with ease
- **Status Tracking** - Monitor task progress with status updates
- **Session Management** - Secure session-based authentication with Flask-Login
- **Responsive Design** - Mobile-friendly UI with HTML and CSS
- **Data Persistence** - Reliable SQLite database for task storage

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Backend language |
| **Flask** | Web framework |
| **Flask-Login** | User session management |
| **SQLite** | Database |
| **HTML/CSS** | Frontend |
| **Werkzeug** | Password hashing & WSGI utilities |

## 📁 Project Structure

```
flask-task-manager/
├── app.py                 # Application initialization
├── models.py              # Database models (User, Task)
├── auth.py                # Authentication logic & routes
├── routes.py              # Task management routes
├── requirements.txt       # Project dependencies
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   └── tasks.html        # Task management page
├── static/                # Static assets
│   ├── css/              # Stylesheets
│   └── js/               # JavaScript files
└── instance/              # Instance-specific files (database, config)
```

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/nikhilkumar-python/flask-task-manager.git
cd flask-task-manager
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Database
```bash
python
>>> from app import app, db
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

### 5. Run the Application
```bash
python app.py
```

The application will be accessible at `http://localhost:5000`

## 💡 Usage

### Create an Account
1. Navigate to the registration page
2. Enter your email and password
3. Click "Register"

### Manage Tasks
1. Log in to your account
2. Click "Add Task" to create a new task
3. View all tasks on the dashboard
4. Edit task details or mark as complete
5. Delete tasks as needed

### Example Task Creation
```
Title: Complete project documentation
Description: Write comprehensive README and API docs
Status: In Progress
Due Date: 2026-02-14
```

## 🔌 API Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|-----------------|
| POST | `/register` | Create new user account | No |
| POST | `/login` | User login | No |
| GET | `/logout` | User logout | Yes |
| GET | `/dashboard` | View all tasks | Yes |
| POST | `/task/add` | Create new task | Yes |
| PUT | `/task/<id>/update` | Update task details | Yes |
| DELETE | `/task/<id>/delete` | Delete task | Yes |

## 🔐 Security Features

- **Password Hashing** - Passwords are hashed using Werkzeug security
- **Session Management** - Secure session cookies with Flask-Login
- **CSRF Protection** - Flask-WTF for form security (recommended)
- **SQL Injection Prevention** - SQLAlchemy ORM prevents SQL injection
- **Authentication Required** - Login required for sensitive operations

## 📚 Learning Outcomes

Through this project, I gained hands-on experience with:

- Modern Flask application architecture and blueprints
- User authentication and authorization patterns
- Relational database design with SQLAlchemy ORM
- CRUD operations and database relationships
- Session management and security best practices
- Writing clean, maintainable, and modular Python code
- Frontend-backend integration

## 🔮 Future Improvements

- [ ] **REST API** - Full RESTful API with JSON responses
- [ ] **JWT Authentication** - Token-based authentication for better scalability
- [ ] **Task Pagination** - Implement pagination for large task lists
- [ ] **Search & Filtering** - Advanced search and filter capabilities
- [ ] **Task Categories** - Organize tasks by categories/projects
- [ ] **Due Date Notifications** - Email reminders for upcoming deadlines
- [ ] **Deployment** - Deploy on Heroku, AWS, or DigitalOcean
- [ ] **Dark Mode** - Add dark theme support
- [ ] **Unit Tests** - Comprehensive test coverage
- [ ] **Docker Support** - Containerization for easy deployment

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Nikhil Kumar**
- GitHub: [@nikhilkumar-python](https://github.com/nikhilkumar-python)

## 📞 Support & Contact

For questions or suggestions, please open an issue on [GitHub Issues](https://github.com/nikhilkumar-python/flask-task-manager/issues).

## 🙏 Acknowledgments

- Flask documentation and community
- SQLAlchemy for excellent ORM support
- Bootstrap for responsive design patterns

---

<div align="center">

**[Back to top](#flask-task-manager)**

Made with ❤️ by Nikhil Kumar

</div>