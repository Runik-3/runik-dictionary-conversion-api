from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/<test>')
def index(test):
    return (test)