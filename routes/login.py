from os import getenv
from flask import Blueprint, jsonify, session
from requests_oauthlib import OAuth2Session

login_blueprint = Blueprint('login_blueprint', __name__)
scope = ['identify', 'email']


@login_blueprint.route("/login", methods=["GET"])
def login():
    oauth = OAuth2Session(getenv("CLIENT_ID"), redirect_uri=getenv("REDIRECT_URL"), scope=scope)
    login_url, state = oauth.authorization_url("https://discordapp.com/api/oauth2/authorize")
    return jsonify({"test": True})
