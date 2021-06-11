from flask import Blueprint

bp = Blueprint('postings', __name__, url_prefix='/postings')

from .import routes