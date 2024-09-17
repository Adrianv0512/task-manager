#ALL REQUIRED LIBRARIES
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

#Creating the database with the 'tasks' table
con = sqlite3.connect("task.db", check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS tasks(name, status)")

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
        if 'taskform' in request.form.keys():
            data =[(request.form.get('taskform'), 'not started')]
            cur.executemany("""
                INSERT INTO tasks VALUES
                        (?, ?)
            """, data)
        print(request.get_data())
        return redirect(url_for('index')) # this is a Response

    # nothing is returned if method is neither get nor post

# test endpoint to go with my test script
@app.route('/test', methods = ["GET", "POST"])
def test():
    if request.method == 'GET':
        return "you hit the get endpoint!!!"
        
    elif request.method == 'POST':
        print("here's the data you posted:")
        for key in request.form:
            print(f"\t{key}, {request.form[key]}")
        return "you hit the post endpoint!!!"

    return "uwu this is a third string to be returned"

#Delete Task Page
#NOT IMPLEMENTED YET
'''
@app.route('/deletetask', methods=['GET', 'POST'])
def deletetask():
    if request.method == 'GET':
        return render_template('delete.html')
    elif request.method == 'POST':
        return 0
'''

#Runs the Application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
