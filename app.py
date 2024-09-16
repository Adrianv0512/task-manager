from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
taskList = []

@app.route('/')
def index():
    return render_template('index.html', tkl=taskList)


@app.route('/addtask', methods=['GET', 'POST'])
def addTask():
    if request.method == 'GET':
        return render_template('add.html')
        
    elif request.method == 'POST':
        if 'taskForm' in request.form.keys():
            taskList.append(request.form.get('taskForm'))
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
