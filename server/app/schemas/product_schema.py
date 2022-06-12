from itertools import product
from app.schemas import ma
from app.models import Product

from marshmallow import fields

class CreateProductSchema(ma.Schema):
    nome = fields.Str(required=True)
    preco = fields.Float(required=True)
    descricao = fields.Str(required=True)

class GetProductSchema(ma.Schema):
    class Meta:
        model = Product
        # fields = ('id', 'nome', 'preco', 'descricao')
    id = fields.Int(required=True)
    nome = fields.Str(required=True)
    preco = fields.Float(required=True)
    descricao = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

class UpdateProductSchema(ma.Schema):
    id = fields.Int(required=True)
    nome = fields.Str(required=True)
    preco = fields.Float(required=True)
    descricao = fields.Str(required=True)


products_list = GetProductSchema(many=True)
product_one = GetProductSchema()