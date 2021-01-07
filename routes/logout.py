from main import discord
from flask import Blueprint, jsonify
from flask_discord import requires_authorization

logout_blueprint = Blueprint("logout_blueprint", __name__)

@logout_blueprint.route("/logout")
@requires_authorization
def logout():
    discord.revoke()
    return jsonify({"error": False})