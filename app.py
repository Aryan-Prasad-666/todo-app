from flask import Flask, render_template, request
import sqlite3
import os

# database_dir = os.getcwd()

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def addtask():
    pass

if __name__ == '__main__':
    app.run(debug=True)