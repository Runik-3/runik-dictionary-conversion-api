from flask import Flask
from flask import Request


app = Flask(__name__)

@app.route('/', methods=["POST"])
def test(): 
    return '<h1>test</h1>'