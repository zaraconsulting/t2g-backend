from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.repo.users.User import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.verify_password_hash(password):
        return user

@token_auth.verify_token
def verify_token(token):
    return User.check_token(token) if token else None
