from flask import Flask, render_template, request
import sqlite3
import os

database_dir = os.getcwd()

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def addtask():
    newtask = request.form['newtask']
    connection = sqlite3.connect(database_dir+"/tasks.db")
    cursor = connection.cursor()


if __name__ == '__main__':
    app.run(debug=True)