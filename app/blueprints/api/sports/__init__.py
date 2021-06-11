from flask import Blueprint

bp = Blueprint('sports', __name__, url_prefix='/sports')

from .import routes