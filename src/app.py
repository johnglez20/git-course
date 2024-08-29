from flask import flask

app = flask(__name__)

@app.route('/hello')
def index():
    return "hello world!"

@app.route('/sum/<int:a>/<int:b>')
def suma(a: int, b: int):
    
    return a+b