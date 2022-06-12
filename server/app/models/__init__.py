from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime,)
    updated_at = db.Column(db.DateTime,)

    def __init__(self, full_name, username, email, password, role, cpf):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role
        self.cpf = cpf,
        self.active = True
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'cpf': self.cpf,
            'active': self.active,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return '<User %r>' % self.username

class Endereco(db.Model):
    __tablename__ = 'endereco'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    cep = db.Column(db.String(80), nullable=False)
    logradouro = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.String(80), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    cidade = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime,)
    updated_at = db.Column(db.DateTime,)
    def __repr__(self):
        return '<Endereco %r>' % self.id

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.Integer(), nullable=False)

    created_at = db.Column(db.DateTime,)
    updated_at = db.Column(db.DateTime,)
    status = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Customer %r>' % self.full_name





class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime,)
    updated_at = db.Column(db.DateTime,)

    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        

    def __repr__(self):
        return '<Product %r>' % self.nome

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(45), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    created_at = db.Column(db.DateTime,)
    updated_at = db.Column(db.DateTime,)

    def __repr__(self):
        return '<Order %r>' % self.id

class OrderProduct(db.Model):
    __tablename__ = 'order_product'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price_total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime,)
    updated_at = db.Column(db.DateTime,)

    def __repr__(self):
        return '<OrderProduct %r>' % self.id

