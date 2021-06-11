
# from flask import jsonify, current_app as app
# from app import db
# from .blueprints.auth import basic_auth
# from .blueprints.auth import token_auth


# @bp.route('/tokens', methods=['POST'])
# @basic_auth.login_required
# def get_token():
#     token = basic_auth.current_user().get_token()
#     db.session.commit()
#     return jsonify({'token': token})


# @bp.route('/tokens', methods=['DELETE'])
# @basic_auth.login_required
# def revoke_token():
#     token_auth.current_user().revoke_token()
#     db.session.commit()
#     return '', 204
