from flask import Flask
from flask import Request


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def test(): 
    if request.method=="GET":
        print ('get')
    return '<h1>test</h1>'