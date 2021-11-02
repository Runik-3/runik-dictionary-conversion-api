from flask import Flask
from flask import request
from dotenv import load_dotenv

from app.helpers.cleanup_helper import cleanup
from app.routes.api_route import api

load_dotenv()


app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index(): 

    print('test')
    # at some point return text instructions for API
    return 'this is /'

app.after_request(cleanup)

if __name__ == '__main__':
    app.run('localhost', 8080)