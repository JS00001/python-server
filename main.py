"""
Python Authentication API
Author: JS
"""

from os import getenv, environ
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_discord import DiscordOAuth2Session
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = getenv("SESSION_SECRET")

#   Flask Configuration
environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
app.config["MONGO_URI"] = getenv("MONGO_URL")
app.config["DISCORD_CLIENT_ID"] = getenv("CLIENT_ID")
app.config["DISCORD_REDIRECT_URI"] = getenv("REDIRECT_URL")
app.config["DISCORD_CLIENT_SECRET"] = getenv("CLIENT_SECRET")

#   Exported Variables
mongo = PyMongo(app)
dbusers = mongo.db.users
dbapikeys = mongo.db.apikeys
dbproducts = mongo.db.products
dbtransactions = mongo.db.transactions
discord = DiscordOAuth2Session(app)

#   Flask Routes
from routes.v1.user import user_blueprint
from routes.v1.login import login_blueprint
from routes.v1.apikey import apikey_blueprint
from routes.v1.logout import logout_blueprint
from routes.v1.products import products_blueprint

app.register_blueprint(products_blueprint)
app.register_blueprint(logout_blueprint)
app.register_blueprint(apikey_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(user_blueprint)

#   Error Handling (404)
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": True, "message": 404})


#   Start Server
if __name__ == "__main__":
    app.run(debug=True)
