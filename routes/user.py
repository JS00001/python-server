from flask import Blueprint, jsonify

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/user/<username>')
def user():
    return jsonify()