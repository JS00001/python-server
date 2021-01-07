"""
Python Authentication API
Author: JS
"""

from os import getenv
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from routes.user import user_blueprint
from routes.login import login_blueprint

load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = getenv("MONGO_URL")
app.register_blueprint(login_blueprint)
mongo = PyMongo(app).db


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": True, "message": 404})


if __name__ == "__main__":
    app.run(debug=True)
