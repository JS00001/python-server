from main import discord, dbusers
from flask import Blueprint, jsonify, redirect
from flask_discord import requires_authorization, Unauthorized

login_blueprint = Blueprint("login_blueprint", __name__)

# Error Handling
@login_blueprint.errorhandler(Unauthorized)
def authorization():
    return jsonify({"error": True})


# Login Route (Redirects to Discord)
@login_blueprint.route("/login")
def login():
    return discord.create_session()


# Callback Route (Processes Data)
@login_blueprint.route("/login/callback")
def callback():
    discord.callback()
    return redirect("http://localhost:5000/login/profile")


# Profile Route (View user data)
@login_blueprint.route("/login/profile")
@requires_authorization
def profile():
    user = discord.fetch_user()
    if not dbusers.find_one({"id": user.id}):
        dbusers.insert_one(
            {
                "id": user.id,
                "username": user.username,
                "avatar": user.avatar_url,
                "admin": False,
                "products": [],
            }
        )
    data = dbusers.find_one({"id": user.id})
    del data["_id"]
    return data
