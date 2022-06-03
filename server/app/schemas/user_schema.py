from app.schemas import ma
from app.models import User

from marshmallow import fields

class RegisterSchema(ma.Schema):
    full_name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    role = fields.Str(required=True)
    cpf = fields.Str(required=True)

class LoginSchema(ma.Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

user_schema = RegisterSchema()






