from main import dbusers
from flask import Blueprint, jsonify

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix='/v1/user')


# Route URL for user data
@user_blueprint.route("/<user_id>")
def user(user_id):
    data = dbusers.find_one_or_404({"id": int(user_id)})
    del data["_id"]
    return data
