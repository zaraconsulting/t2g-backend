from app import db
from .import bp as positions
from flask import jsonify, request
from datetime import datetime as dt
from flask_login import login_required, current_user
from app.blueprints.api.auth.auth import token_auth
from app.repo.positions.Position import Position


@positions.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /positions/
    """
    return jsonify([p.to_dict() for p in Position.query.all()])


@positions.route('/<int:id>')
@token_auth.login_required
def get_position(id):
    """
    [GET] /positions/<id>
    """
    return jsonify(Position.query.get(id).to_dict())


@positions.route('/create', methods=['POST'])
@token_auth.login_required
def create_position():
    """
    [POST] /positions/
    """
    data = request.json
    p = Position()
    p.from_dict(data)
    p.save()
    return jsonify(p.to_dict()), 201


@positions.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_position(id):
    """
    [PUT] /positions/
    """

    data = request.json
    p = Position(id)
    p.from_dict(data)
    p.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(p.to_dict()), 201


@positions.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_position(id):
    """
    [DELETE] /positons/
    """

    p = p.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify([p.to_dict() for p in Position.query.all()])
