from flask import Blueprint, jsonify, request
from models.apikeys import Apikey
from main import dbapikeys
import random, string, json

apikey_blueprint = Blueprint('apikey_blueprint', __name__, url_prefix="/v1/apikey")

# List All Api Keys
@apikey_blueprint.route('/list', methods=["GET"])
def apikey_list():
    keys =[]
    for document in dbapikeys.find():
        del document['_id']
        keys.append(document)
    return jsonify(keys)

# Generate Api Keys
@apikey_blueprint.route('/create', methods=['POST'])
def apikey_create():
    letters = string.ascii_letters
    data = json.loads(request.data)
    randomstr = ''.join(random.choice(letters) for i in range(16))
    api = Apikey(
        randomstr,
        data['permissions']
    )
    api.save()
    return jsonify(api.pull())

# Delete Api Keys
@apikey_blueprint.route('/delete', methods=['DELETE'])
def apikey_delete():
    data = request.args
    api_object = dbapikeys.find_one({"key": data['key']})
    if not api_object:
        return jsonify({"error": True, "message": "Not Found"})
    dbapikeys.delete_one({"key": data['key']})
    return jsonify({"error": False})

# Add Perms to Api Key
@apikey_blueprint.route('/update', methods=['PUT'])
def apikey_update():
    data = json.loads(request.data)
    for perm in data['permissions']:
        dbapikeys.update_one({"key": data['key']}, {'$push': {'permissions': perm}})
    return jsonify({"error": False})