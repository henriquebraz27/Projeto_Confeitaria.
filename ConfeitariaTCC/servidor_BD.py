#rodar e acessar pelo Firefox (ou chrome)
#se voce não conseguir rodar, talvez seja a falta da biblioteca.
#nesse caso, rode no CMD: pip install flask --user
#MAC ou Linux: pip3 install flask --user

from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from decimal import Decimal


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:*Braz2702@localhost/confeitaria'  #root= seu usuario
                                                                                    
db=SQLAlchemy(app)

@app.route("/carrinho/")
def carrin():
    prod = Produtos.query.filter_by(id=2).first()
    return render_template("carrinho.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pedidos/")   
def ped():
    return render_template("pedidos.html")


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = usuarios.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            #imprimit mensagem de erro
            return render_template('login.html')
        
        return render_template('homelogado.html')
        
    
    return render_template('login.html')




class usuarios(db.Model):
    _tablename_ = 'usuarios'
    idconta = db.Column(db.Integer, primary_key=True, autoincrement=True)
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

@app.route("/cadastro/", methods=["GET","POST"])
def cadastrar():
    if request.method == "POST":
        nome=request.form["txtnome"]
        email=request.form["txtemail"]
        senha=request.form["txtsenha"]
        a = usuarios(nome,email,senha)
        db.session.add(a)
        db.session.commit()
        return render_template("homelogado.html")
    return render_template("cadastro.html")



class Carrinho (db.Model):
    _tablename_ = 'Carrinho'
    idcompra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data=db.Column(db.String(55)) 
    valortotal= db.Column(db.String(20))
    def _init_(self, produto,valor,quantidade):
        self.produto=produto
        self.valor=valor
        self.quantidade=quantidade



class Produtos (db.Model):
    _tablename_ = 'Produtos'
    idproduto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    produto=db.Column(db.String(55)) 
    valor= db.Column(db.String(20))
    quantidade=db.Column(db.String(20))
    def _init_(self, produto,valor,quantidade):
        self.produto=produto
        self.valor=valor
        self.quantidade=quantidade




db.create_all()

if __name__ == "__main__":
    
    app.run(debug=True)