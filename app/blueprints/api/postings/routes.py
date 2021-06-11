from app import db
from .import bp as postings
from flask import jsonify, request
from datetime import datetime as dt
from app.repo.postings.Posting import Posting
from flask_login import login_required, current_user
from app.blueprints.api.auth.auth import token_auth


@postings.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /postings/
    """
    return jsonify([p.to_dict() for p in Posting.query.all()])


@postings.route('/<int:id>')
@token_auth.login_required
def get_posting(id):
    """
    [GET] /postings/<id>
    """
    return jsonify(Posting.query.get(id).to_dict())


@postings.route('/create', methods=['POST'])
@token_auth.login_required
def create_posting():
    """
    [POST] /postings/
    """
    data = request.json
    p = Posting()
    p.from_dict(data)
    p.save()
    return jsonify(p.to_dict()), 201


@postings.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_posting(id):
    """
    [PUT] /postings/
    """

    data = request.json
    p = Posting(id)
    p.from_dict(data)
    p.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(p.to_dict()), 201


@postings.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_posting(id):
    """
    [DELETE] /postings/
    """

    p = p.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify([p.to_dict() for p in Posting.query.all()])
