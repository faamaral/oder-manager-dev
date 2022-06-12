from datetime import datetime
from itertools import product
from flask import Blueprint, jsonify, make_response, request
from marshmallow import ValidationError
from sqlalchemy.exc import StatementError

from app.schemas.product_schema import CreateProductSchema, UpdateProductSchema, products_list, product_one
from app.models import Product, db

product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.route('/create', methods=['POST'])
def create():
    try:
        product_data = CreateProductSchema().loads(request.data)
    except ValidationError as err:
        return make_response(err.messages, 400)
    
    try:
        product = Product(product_data['nome'], product_data['preco'], product_data['descricao'])
        db.session.add(product)
        db.session.commit()
        return make_response(jsonify({
            'message': 'Product created successfully',
            'status': 201
        }), 201)
    except StatementError as err:
        return make_response(err.statement, 400)

@product_bp.route('/update/<id>', methods=['PUT'])
def update(id):
    try:
        product_data = UpdateProductSchema().loads(request.data)
    except ValidationError as err:
        return make_response(err.messages, 422)
    try:
        product = Product.query.get(id)
        if 'nome' in product_data:
            product.nome = product_data['nome']
        if 'preco' in product_data:
            product.preco = product_data['preco']
        if 'descricao' in product_data:
            product.descricao = product_data['descricao']
        product.updated_at = datetime.now()
        db.session.add(product)
        db.session.commit()
        return make_response(jsonify({
            'message': 'Product updated successfully',
            'status': 200
        }), 200)
    except StatementError as err:
        return make_response(err.statement, 400)

@product_bp.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    try:
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return make_response(jsonify({
            'message': 'Product deleted successfully',
            'status': 200
        }), 200)
    except StatementError as err:
        return make_response(err.statement, 400)

@product_bp.route('/all', methods=['GET'])
def all():
    try:
        products = Product.query.all()
    except StatementError as err:
        return make_response(err.statement, 400)
    
    return make_response(jsonify(products_list.dump(products)), 200)
@product_bp.route('/view/<id>', methods=['GET'])
def view(id):
    try:
        product = Product.query.get(id)
    except StatementError as err:
        return make_response(err.statement, 400)
    return make_response(jsonify(product_one.dump(product)), 200)