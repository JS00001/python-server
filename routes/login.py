from main import discord
from flask import Blueprint, jsonify, redirect
from flask_discord import requires_authorization

login_blueprint = Blueprint("login_blueprint", __name__)

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
    return user.name
