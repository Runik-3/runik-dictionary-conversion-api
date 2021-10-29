from typing import Sequence
from flask import Blueprint
from flask import request
from flask.wrappers import Response
from werkzeug.utils import send_file

from app.controllers.dictionary_controller import dictionary_handler

api = Blueprint('api', __name__)


@api.route('/<target_device>/<input_format>/<dictionary_title>', methods=["POST"])
def index(target_device, dictionary_title, input_format, request = request):

    output_path = dictionary_handler(target_device, dictionary_title, input_format, request)
    res = open(output_path, 'r')

    return Response(res.read())