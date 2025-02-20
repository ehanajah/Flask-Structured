from flask import request
from . import blogsBlueprint
from .service import index

    
@blogsBlueprint.route('/', methods=['GET'])
def index():
    return index()
        
    