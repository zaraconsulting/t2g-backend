from flask import Blueprint

bp = Blueprint('available_videos', __name__, url_prefix='/available_videos')

from .import routes