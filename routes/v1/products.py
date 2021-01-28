from decorators.apiauth import api_authentication
from models.products import Product
from flask import jsonify, Blueprint, request
import json

products_blueprint = Blueprint("product_blueprint", __name__, url_prefix='/v1/products')

@products_blueprint.route("/add", methods=['POST'])
@api_authentication("MANAGE_PRODUCTS")
def products():
    data = json.loads(request.data)
    product = Product(
        data['name'],
        data['category'],
        data['description'],
        data['price']
    )
    product.save()
    return jsonify(data)

@products_blueprint.route("/remove", methods=['DELETE'])
@api_authentication("MANAGE_PRODUCTS")
def products2():
    return jsonify({"a": "a"})

@products_blueprint.route("/list", methods=['GET'])
@api_authentication("MANAGE_PRODUCTS")
def products3():
    return jsonify({"a": "a"})

