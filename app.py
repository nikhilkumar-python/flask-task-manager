# Updated app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
import logging
import sqlite3

# Initialize logging
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Enable CSRF protection
csrf = CSRFProtect(app)

# Database initialization
def init_db():
    with sqlite3.connect('your_database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT, done BOOLEAN)''')
        logging.info('Database initialized successfully.')

@app.route('/')
def index():
    with sqlite3.connect('your_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
@csrf.exempt
def add_task():
    task_name = request.form['name']
    with sqlite3.connect('your_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (name, done) VALUES (?, ?)', (task_name, False))
        conn.commit()
        logging.info(f'Task added: {task_name}')  
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    try:
        with sqlite3.connect('your_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            conn.commit()
            logging.info(f'Task deleted: {task_id}')
        flash('Task deleted successfully!')
    except Exception as e:
        logging.error(f'Error deleting task: {e}')
        flash('An error occurred while trying to delete the task.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)