from flask import Flask
from flask import request
from dotenv import load_dotenv

from routes.api_route import api

load_dotenv()


app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index(): 
    # at some point return text instructions for API
    return 'this is /'


if __name__ == '__main__':
    app.run('localhost', 8080)