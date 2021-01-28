from main import discord
from flask import Blueprint, jsonify
from flask_discord import requires_authorization

logout_blueprint = Blueprint("logout_blueprint", __name__, url_prefix='/v1/logout')

# Route URL for logout
@logout_blueprint.route("/")
@requires_authorization
def logout():
    discord.revoke()
    return jsonify({"error": False})
