from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import time


con = mysql.connector.connect(host='localhost',database='confeitaria',user='root',password='')


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/confeitaria'
db=SQLAlchemy(app)



class Carrinho (db.Model):
    _tablename_ = 'Carrinho'
    idcompra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    produto=db.Column(db.String(55)) 
    valor= db.Column(db.String(20))
    quantidade=db.Column(db.Integer(20))
    def _init_(self, produto,valor,quantidade):
        self.produto=produto
        self.valor=valor
        self.quantidade=quantidade
    
    def comprando(self,quantidade):
        cursor = con.cursor()
        cursor.execute("\nselect * from  Carrinho;\n")



    
db.create_all()

prod="Agua Mineral"
prec="20,00"
a = Carrinho(prod,prec)
db.session.add(a)
db.session.commit()

