from app import db
from flask_login import login_required, current_user
from app.blueprints.api.auth.auth import token_auth
from .import bp as available_videos
from flask import jsonify, request
from datetime import datetime as dt
from app.repo.available_videos.Available_videos import Available_Videos


@available_videos.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /available_videos/
    """
    return jsonify([a.to_dict() for a in Available_Videos.query.all()])


@available_videos.route('/<int:id>')
@token_auth.login_required
def get_video(id):
    """
    [GET] /available_videos/<id>
    """
    return jsonify(Available_Videos.query.get(id).to_dict())


@available_videos.route('/create', methods=['POST'])
@token_auth.login_required
def create_video():
    """
    [POST] /available_videos/
    """
    data = request.json
    a = Available_Videos()
    a.from_dict(data)
    a.save()
    return jsonify(a.to_dict()), 201


@available_videos.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_video(id):
    """
    [PUT] /available_videos/
    """

    data = request.json
    a = Available_Videos(id)
    a.from_dict(data)
    a.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(a.to_dict()), 201


@available_videos.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_video(id):
    """
    [DELETE] /available_videos/
    """

    a = a.query.get(id)
    db.session.delete(a)
    db.session.commit()
    return jsonify([a.to_dict() for a in Available_Videos.query.all()])
