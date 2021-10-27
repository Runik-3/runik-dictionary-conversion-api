from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def test(): 
    if request.method=="GET":
        print ('get')
    else: 
        print ('post')
    return '<h1>test</h1>'