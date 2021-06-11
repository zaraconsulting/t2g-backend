from app import db, login_manager
import os, base64
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, timedelta


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, index=True, unique=True)
    password = db.Column(db.String)
    roles = db.relationship('Role', backref='user', lazy='dynamic')
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime())

    def create_password_hash(self, password):
        self.password = generate_password_hash(password)

    def verify_password_hash(self, password_to_verify):
        return check_password_hash(self.password, password_to_verify)

    def save(self):
        self.create_password_hash(self.password)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<User: {self.email}>'

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String, unique=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

