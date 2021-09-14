from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/confeitaria'
db=SQLAlchemy(app)



class usuarios(db.Model):
    _tablename_ = 'userss'
    idconta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email=db.Column(db.String(550)) 
    senha = db.Column(db.String(20))
    def _init_(self, email,senha):
        self.email=email
        self.senha=senha
        
db.create_all()