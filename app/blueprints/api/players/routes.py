from app import db
from .import bp as players
from flask import jsonify, request
from app.blueprints.api.auth.auth import token_auth
from datetime import datetime as dt
from flask_login import login_required, current_user
from app.blueprints.api.auth.auth import token_auth
from app.repo.players.Player import Player


@players.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /players/
    """
    return jsonify([p.to_dict() for p in Player.query.all()])


@players.route('/<int:id>')
@token_auth.login_required
def get_player(id):
    """
    [GET] /players/<id>
    """
    return jsonify(Player.query.get(id).to_dict())


@players.route('/create', methods=['POST'])
@token_auth.login_required
def create_player():
    """
    [POST] /players/
    """
    data = request.json
    p = Player()
    p.from_dict(data)
    p.save()
    return jsonify(p.to_dict()), 201


@players.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_player(id):
    """
    [PUT] /players/
    """

    data = request.json
    p = Player(id)
    p.from_dict(data)
    p.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(p.to_dict()), 201


@players.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_player(id):
    """
    [DELETE] /players/
    """

    p = p.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify([p.to_dict() for p in Player.query.all()])
