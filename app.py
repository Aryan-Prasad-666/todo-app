from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

database_dir = os.getcwd()

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    connection = sqlite3.connect(database_dir+"/tasks.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasklist')
    tasks = cursor.fetchall() 
    connection.close()
    return render_template("index.html", tasks=tasks)

@app.route('/', methods=['POST'])
def addtask():
    newtask = request.form['newtask']
    connection = sqlite3.connect(database_dir+"/tasks.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO tasklist (task) VALUES (?)', (newtask,))
    connection.commit()
    connection.close()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)