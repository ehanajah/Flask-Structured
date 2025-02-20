from flask import request
from app.utils import method_unavailable

from . import authorsBlueprint
from .service import index, show, store, update, destroy


@authorsBlueprint.route('/', methods=['GET', 'POST'])
def index():
    match request.method:
        case 'GET':
            return index()
        case 'POST':
            return store(request)
        case _:
            return method_unavailable(request.method)


@authorsBlueprint.route('/<int:id>', methods=["GET", "PUT", "DELETE"])
def author_handler(id):
    match request.method:
        case 'GET':
            return show(id)
        case 'PUT':
            return update(request, id)
        case 'DELETE':
            return destroy(id)
        case _:
            return method_unavailable(request.method)
