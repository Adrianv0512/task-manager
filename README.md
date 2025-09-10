# Task Manager Web App

A simple Flask + SQLite task manager that allows users to add, update, and delete tasks through a clean web interface. Designed as a lightweight productivity tool and as a demonstration of full-stack development fundamentals.

# Features

Add tasks with custom names

Update task status (e.g., Not Started → In Progress → Completed)

Delete tasks from the database

SQLite backend for persistent storage

Flask web server with templated HTML pages (index, add, update, delete)

Bootstrap support for styling (CSS/JS in /static)

# Tech Stack

Backend: Python, Flask

Database: SQLite3

Frontend: HTML, Jinja2 templates, Bootstrap (CSS/JS)

Environment: Virtualenv (recommended)

# Getting Started
1. Clone the repo
git clone https://github.com/adrianv0512/task-manager.git
cd task-manager

2. Create & activate a virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
OR
venv\Scripts\activate          # Windows CMD/PowerShell

3. Install dependencies
pip install flask

4. Run the app
python app.py

5. Open in browser

Navigate to:
http://127.0.0.1:5000/

# Future Improvements

User authentication (login system)

Task due dates & reminders

Priority levels (high/medium/low)

Search/filter tasks

Cloud deployment (Heroku/Render)

# License

This project is licensed under the MIT License — feel free to use and adapt it.
