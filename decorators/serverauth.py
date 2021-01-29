from functools import wraps
from main import dbapikeys
from flask import request, jsonify

def server_authentication(func):
    @wraps(func)
    def decorater(*args, **kwargs):
        return func(*args, **kwargs)
    return decorater


