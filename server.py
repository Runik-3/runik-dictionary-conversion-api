from flask import Flask
from flask import request
from dotenv import load_dotenv
from flask_cors import CORS

from app.helpers.cleanup_helper import cleanup
from app.routes.api_route import api

from pyglossary.glossary import Glossary

load_dotenv()

Glossary.init()


app = Flask(__name__)
CORS(app)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index(): 

    # at some point return text instructions for API
    return 'this is /'

#app.after_request(cleanup)

if __name__ == '__main__':
    app.run('localhost', 8080)