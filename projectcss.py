from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo

app= Flask(__name__)

@app.route('/css')
def display():
    return render_template('css.html')

if __name__ == '__main__':
    app.run(debug = True)
