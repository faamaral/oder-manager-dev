from datetime import datetime, timedelta
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import create_access_token, create_refresh_token
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError, StatementError

from app.models import User
from app.models import db

from app.schemas.user_schema import RegisterSchema, LoginSchema

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['POST', 'GET'])
def register():
    try:
        user_data = RegisterSchema().loads(request.data)
    except ValidationError as err:
        return make_response(err.messages, 400)

    try:
        user = User(
            full_name=user_data['full_name'],
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'],
            role=user_data['role'],
            cpf=user_data['cpf']
        )
        db.session.add(user)
        db.session.commit()

        return make_response(jsonify({
            'message': 'User created successfully',
            'status': 201
        }), 201)
    except StatementError as err:
        return make_response(err.statement, 400)


@auth.route('/login', methods=['POST'])
def login():
    try:
        user_data = LoginSchema().loads(request.data)
    except ValidationError as err:
        return make_response(err.messages, 400)

    user = User.query.filter_by(username=user_data['username']).first()
    if user and user.verify_password(user_data['password']):

        access_token = create_access_token(
            identity=user.id, expires_delta=timedelta(days=5))
        refresh_token = create_refresh_token(identity=user.id)
        return make_response(jsonify({
            'message': 'Logged in successfully',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'status': 201
        }), 201)

    return make_response(jsonify({
        'message': 'Invalid credentials',
        'status': 401
    }), 401)
