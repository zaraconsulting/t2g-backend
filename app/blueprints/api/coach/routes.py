from app import db
from .import bp as coaches
from flask_login import login_required, current_user
from app.blueprints.api.auth.auth import token_auth
from flask import jsonify, request
from datetime import datetime as dt
from app.repo.coaches.Coach import Coach

@coaches.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /coaches/
    """
    return jsonify([c.to_dict() for c in Coach.query.all()])

@coaches.route('/<int:id>')
@token_auth.login_required
def get_coach(id):
    """
    [GET] /coaches/<id>
    """
    return jsonify(Coach.query.get(id).to_dict())

@coaches.route('/create', methods=['POST'])
@token_auth.login_required
def create_coach():
    """
    [POST] /coaches/
    """
    data = request.json
    c = Coach()
    c.from_dict(data)
    c.save()
    return jsonify(c.to_dict()), 201


@coaches.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_coach(id):
    """
    [PUT] /coaches/
    """

    data = request.json
    c = Coach(id)
    c.from_dict(data)
    c.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(c.to_dict()), 201


@coaches.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_coach(id):
    """
    [DELETE] /coaches/
    """

    c = c.query.get(id)
    db.session.delete(c)
    db.session.commit()
    return jsonify([c.to_dict() for c in Coach.query.all()])
