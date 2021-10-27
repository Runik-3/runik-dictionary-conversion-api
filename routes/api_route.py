from os import write
from flask import Blueprint
from flask import request

from app.services.write_data_file_service import write_data_to_file

api = Blueprint('api', __name__)


@api.route('/<target_device>/<dictionary_title>', methods=["POST"])
def index(target_device, dictionary_title):
    dict_data = request.get_data()
    write_data_file(dict_data, dictionary_title)

    return (f'{target_device} {dictionary_title}')