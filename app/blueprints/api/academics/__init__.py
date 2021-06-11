from flask import Blueprint

bp = Blueprint('academics', __name__, url_prefix='/academics')

from .import routes