from flask import current_app as app, jsonify

@app.route('/')
def index():
    return jsonify({ 'message': 'It works!' })