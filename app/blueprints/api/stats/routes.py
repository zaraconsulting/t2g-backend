from app import db
from flask import jsonify, request
from datetime import datetime as dt
from app.repo.stats.Stat import Stat
from .import stats as bp
from flask_login import login_required, current_user
from app.blueprints.api.auth.auth import token_auth


@bp.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /stats/
    """
    return jsonify([s.to_dict() for s in Stat.query.all()])


@bp.route('/<int:id>')
@token_auth.login_required
def get_stats(id):
    """
    [GET] /stats/<id>
    """
    return jsonify(Stat.query.get(id).to_dict())


@bp.route('/create', methods=['POST'])
@token_auth.login_required
def create_stats():
    """
    [POST] /stats/
    """
    data = request.json
    s = Stat()
    s.from_dict(data)
    s.save()
    return jsonify(s.to_dict()), 201


@bp.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_stats(id):
    """
    [PUT] /stats/
    """

    data = request.json
    s = Stat.query.get(id)
    s.from_dict(data)
    s.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(s.to_dict()), 201


@bp.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_stats(id):
    """
    [DELETE] /stats/
    """

    s = s.query.get(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify([s.to_dict() for s in Stat.query.all()])
