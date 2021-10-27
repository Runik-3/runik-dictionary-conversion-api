from flask import Flask
from flask import request
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def test(): 
    if request.method == "GET":
        print('hi')
    return 'hello'



if __name__ == '__main__':
    app.run('localhost', 8080)