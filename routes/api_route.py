from os import write
from re import T
from flask import Blueprint
from flask import request

from app.controllers.dictionary_controller import dictionary_handler

api = Blueprint('api', __name__)


@api.route('/<target_device>/<input_format>/<dictionary_title>', methods=["POST"])
def index(target_device, dictionary_title, input_format, request = request):

    dictionary_handler(target_device, dictionary_title, input_format, request)

    return(f'{target_device} {dictionary_title}')