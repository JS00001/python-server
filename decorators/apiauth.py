from functools import wraps
from main import dbapikeys
from flask import request, jsonify

def check_auth(key, perm):
    api_object = dbapikeys.find_one({'key': key})
    if api_object and perm in api_object['permissions'] :
        return True
    else:
        return False


def api_authentication(perm):
    def inner_decorator(func):
        @wraps(func)
        def decorater(*args, **kwargs):
            auth = request.headers.get('api-key')
            if not auth or not check_auth(auth, perm):
                return jsonify({'error': True, 'message': 'No Access'})
            return func(*args, **kwargs)
        return decorater
    return inner_decorator


