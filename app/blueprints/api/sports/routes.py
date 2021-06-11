from app import db
from .import bp as sports
from flask import jsonify, request
from datetime import datetime as dt
from flask_login import login_required, current_user
from app.blueprints.api.auth.auth import token_auth
from app.repo.sports.Sport import Sport


@sports.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /sports/
    """
    return jsonify([s.to_dict() for s in Sport.query.all()])


@sports.route('/<int:id>')
@token_auth.login_required
def get_sport(id):
    """
    [GET] /sports/<id>
    """
    return jsonify(Sport.query.get(id).to_dict())


@sports.route('/create', methods=['POST'])
@token_auth.login_required
def create_sport():
    """
    [POST] /players/
    """
    data = request.json
    s = Sport()
    s.from_dict(data)
    s.save()
    return jsonify(s.to_dict()), 201


@sports.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_sport(id):
    """
    [PUT] /sports/
    """

    data = request.json
    s = Sport(id)
    s.from_dict(data)
    s.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(s.to_dict()), 201


@sports.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_sport(id):
    """
    [DELETE] /sports/
    """

    s = s.query.get(id)
    db.session.delete(s)
    db.session.commit()
    return jsonify([s.to_dict() for s in Sport.query.all()])
