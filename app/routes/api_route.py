from typing import Sequence
from flask import Blueprint
from flask import request
from flask.wrappers import Response
from flask import send_file
from os import path
from flask_cors import cross_origin

from app.helpers.cleanup_helper import cleanup
from app.controllers.dictionary_controller import dictionary_handler

api = Blueprint('api', __name__)

@api.route('/')
def test(): 
    return 'hello'

@api.route('/<target_device>/<input_format>/<dictionary_title>', methods=["POST"])
def index(target_device, dictionary_title, input_format, request = request):
    
    print('Processing Dictionary')
    

    output_path = dictionary_handler(target_device, dictionary_title, input_format, request)

    print(output_path)

    if output_path: 
        print('Sending dictionary to client')
        return  send_file(output_path, "appication/zip")
    else: 
        return 'error converting dictionary'
