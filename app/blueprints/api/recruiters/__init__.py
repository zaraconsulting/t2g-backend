from flask import Blueprint

bp = Blueprint('recruiters', __name__, url_prefix='/recruiters')

from .import routes
