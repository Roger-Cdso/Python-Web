from flask import Flask

app = Flask('meu app')

@app.route('/')
def ola():
    return "ola mundo"

@app.route('/novo')
def novo():
    return "<h1>novo</h1>"