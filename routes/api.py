from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/<device>/<title>', methods=["POST"])
def index(device, title):
    return (f'{device} {title}')