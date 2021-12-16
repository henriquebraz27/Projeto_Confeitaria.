from app import db

from flask_login import UserMixin

class Carrinho(db.Model):
    _tablename_ = 'Carrinho'
    idcompra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data=db.Column(db.String(55)) 
    valortotal= db.Column(db.String(20))
    def _init_(self, produto,valor,quantidade):
        self.produto=produto
        self.valor=valor
        self.quantidade=quantidade

class Produtos(db.Model):
    _tablename_ = 'Produtos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome=db.Column(db.String(55)) 
    descricao=db.Column(db.String(255)) 
    imagem=db.Column(db.String(255))
    valor=db.Column(db.String(20))
    
    def _init_(self, id, nome, descricao, imagem, valor):
        self.id=id
        self.nome=nome
        self.descricao=descricao
        self.imagem=imagem
        self.valor=valor

class Usuarios(UserMixin, db.Model):
    _tablename_ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20))
    email=db.Column(db.String(50)) 
    senha = db.Column(db.String(20))
    def __init__(self,nome,email,senha):
        self.nome=nome
        self.email=email
        self.senha=(senha)

    def verify_password(self, pwd):
        return (self.senha, pwd)

db.create_all()