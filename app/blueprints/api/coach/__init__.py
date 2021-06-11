from flask import Blueprint

bp = Blueprint('coaches', __name__, url_prefix='/coaches')

from .import routes