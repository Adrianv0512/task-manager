#ALL REQUIRED LIBRARIES
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

#Creating the database with the 'tasks' table
con = sqlite3.connect("task.db", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS tasks(id, name, status)")

idcount = 0

def reorderID():
    global idcount
    idcount = 0
    idl = []
    data = cur.execute("SELECT id, name, status FROM tasks").fetchall()
    for i in range(len(data)):
        idl.append((idcount, data[idcount][0], data[idcount][1]))
        idcount += 1
    for task in data:
        cur.execute("UPDATE tasks SET id=(?) WHERE id=(?) AND name=(?)", idl[0])
    print(idl)

#Creating the flask application
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

#Index page
@app.route('/')
def index():
    return render_template('index.html', tkl=cur.execute("SELECT name, status FROM tasks"))

#Add task page
#When user submits the form updates tasks table to include new information
# my pylance is angry that this function doesn't return the same thing each time
@app.route('/addtask', methods=['GET', 'POST'])
def addTask():
    if request.method == 'GET':
        return render_template('add.html') # this is a string
        
    elif request.method == 'POST':
        global idcount
        if 'taskform' in request.form.keys():
            data =[(idcount, request.form.get('taskform'), 'Not Started')]
            cur.executemany("""
                INSERT INTO tasks VALUES
                        (?, ?, ?)
            """, data)
            idcount = idcount + 1
        return redirect(url_for('index'))

#Delete Task Page
#When user submits form and sends post request after clicking X button, deletes the task and updates page
@app.route('/deletetask', methods=['GET', 'POST'])
def deletetask():
    if request.method == 'GET':
        return render_template('delete.html', tkl=cur.execute("SELECT id, name, status FROM tasks"))
    elif request.method == 'POST':
        data = cur.execute("SELECT id, name, status FROM tasks").fetchall()
        index = list(request.form.keys())
        print(index)
        print(data)
        cur.execute("DELETE FROM tasks WHERE id=(?) AND name=(?) AND status=(?)", data[int(index[0])])
        reorderID()
        return redirect(url_for('index'))

@app.route('/updatetask', methods=['GET', 'POST'])
def updatetask():
    if request.method == 'GET':
        return render_template('update.html', tkl=cur.execute("SELECT id, name, status FROM tasks"))
    elif request.method == 'POST':
        data = cur.execute("SELECT id, name, status FROM tasks").fetchall()
        status = list(request.form.keys())
        statl =[status[0], int(request.form.get(status[0]))]
        print(statl)
        cur.execute("UPDATE tasks SET status=(?) WHERE id=(?)", statl)
        print(cur.execute("SELECT id, name, status FROM tasks").fetchall())
        return redirect(url_for('index'))


#Runs the Application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
