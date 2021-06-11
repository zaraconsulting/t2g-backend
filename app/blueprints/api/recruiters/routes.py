from app import db
from .import bp as recruiters
from flask import jsonify, request
from datetime import datetime as dt
from flask_login import login_required, current_user
from app.blueprints.api.auth.auth import token_auth
from app.repo.recruiters.Recruiter import Recruiter


@recruiters.route('/', methods=['GET'])
@token_auth.login_required
def index():
    """
    [GET] /recruiters/
    """
    return jsonify([r.to_dict() for r in Recruiter.query.all()])


@recruiters.route('/<int:id>')
@token_auth.login_required
def get_recruiter(id):
    """
    [GET] /recruiters/<id>
    """
    return jsonify(Recruiter.query.get(id).to_dict())


@recruiters.route('/create', methods=['POST'])
@token_auth.login_required
def create_recruiter():
    """
    [POST] /recruiters/
    """
    data = request.json
    r = Recruiter()
    r.from_dict(data)
    r.save()
    return jsonify(r.to_dict()), 201


@recruiters.route('/edit/<int:id>', methods=['PUT'])
@token_auth.login_required
def edit_recruiter(id):
    """
    [PUT] /recruiters/
    """

    data = request.json
    r = Recruiter(id)
    r.from_dict(data)
    r.date_updated = dt.utcnow()
    db.session.commit()
    return jsonify(r.to_dict()), 201


@recruiters.route('/delete/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_recruiterx(id):
    """
    [DELETE] /recruiters/
    """

    r = r.query.get(id)
    db.session.delete(r)
    db.session.commit()
    return jsonify([r.to_dict() for r in Recruiter.query.all()])
