# Flask Task Manager

A task management web application built using Flask that allows users to
register, log in, and manage their daily tasks securely.

## Features
- User registration and authentication
- Create, update, delete tasks
- Task status tracking
- Secure password hashing
- Session-based authentication

## Tech Stack
- Python
- Flask
- SQLite
- HTML, CSS
- Flask-Login

## Project Structure
The application follows a modular structure to improve maintainability:
- routes.py handles URL routing
- models.py manages database models
- auth.py manages authentication logic

## Installation & Setup
1. Clone the repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run the application:
   python run.py

## What I Learned
- Flask application structuring
- Authentication and authorization
- CRUD operations with relational databases
- Writing cleaner, modular Python code

## Future Improvements
- REST API version of this app
- JWT-based authentication
- Pagination and search
- Deployment on cloud
