from flask import flask

app = flask(__name__)

@app.route('/')
def index():
    return "bye code!"

@app.route('/sum/<int:a>/<int:b>')
def suma(a: int, b: int):
    return a+b