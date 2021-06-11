from app import db
from app.blueprints.api.auth.auth import token_auth
from flask_login import login_required, current_user
from .import bp as academics
from flask import jsonify, request
from datetime import datetime as dt
from app.repo.academics.Academics import Academics


@academics.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /academics/
    """
    return jsonify([a.to_dict() for a in Academics.query.all()])


@academics.route('/<int:id>')
@token_auth.login_required
def get_academics(id):
    """
    [GET] /academics/<id>
    """
    return jsonify(Academics.query.get(id).to_dict())


@academics.route('/create', methods=['POST'])
@token_auth.login_required
def create_academics():
    """
    [POST] /academics/
    """
    data = request.json
    a = Academics()
    a.from_dict(data)
    a.save()
    return jsonify(a.to_dict()), 201


@academics.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_academics(id):
    """
    [PUT] /academics/
    """

    data = request.json
    a = Academics(id)
    a.from_dict(data)
    a.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(a.to_dict()), 201


@academics.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_academics(id):
    """
    [DELETE] /academics/
    """

    a = a.query.get(id)
    db.session.delete(a)
    db.session.commit()
    return jsonify([a.to_dict() for a in Academics.query.all()])
