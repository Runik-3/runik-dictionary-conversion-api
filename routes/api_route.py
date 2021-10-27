from os import write
from flask import Blueprint
from flask import request

from app.services.write_data_file_service import write_data_file 
from app.services.convert_dictionary_service import convert_dictionary

api = Blueprint('api', __name__)


@api.route('/<target_device>/<dictionary_title>', methods=["POST"])
def index(target_device, dictionary_title):
    dict_data = request.get_data().decode('utf-8')

    # writes incoming dict to file to be converted 
    write_data_file(dict_data)

    #converts incoming dict from XDXF to the correct format 
    convert_dictionary(target_device, dictionary_title)

    return (f'{target_device} {dictionary_title}')