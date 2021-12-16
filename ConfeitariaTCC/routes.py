# routes.py

import flask
from flask import render_template, session, request
from app import app
from models import Produtos, Usuarios, Carrinho
from app import db
from flask_login import current_user, UserMixin, LoginManager, login_required, login_user, logout_user

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    try:
        return Usuarios.query.filter_by(id=id).first()
    except:
        return None


@app.route("/")
def index():
    produtos = Produtos.query.limit(3).all()
    return render_template("index.html", produtos = produtos)

@app.route("/confirmar/", methods=['POST'])
def confirmar():
    pagamento = request.form['pagamento']
    print(pagamento)

    if len(session['myCarrinho']['produtos']) == 0:
        return render_template('pedido-realizado.html', error='Por favor, você precisa adicionar itens ao seu carrinho antes de finalizar o pedido.')    

    session.pop('myCarrinho')
    return render_template('pedido-realizado.html', sucesso=True)

@app.route("/carrinho/")
def carrinho():
    if not 'myCarrinho' in session:
        session['myCarrinho'] = {
            'address': '',
            'number': '',
            'complement': '',
            'produtos': {},
            'valorTotal': 0,
            'valorTotalComFrete': 8
        }

    ## session.clear()

    carrinho = session['myCarrinho']
    produtos = carrinho['produtos']

    if 'addItem' in request.args:
        id = request.args.get('addItem')

        if not id in produtos:
            produto = Produtos.query.filter_by(id=id).first()

            produtos[id] = {
                'quantity': 1,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'valor': produto.valor
            }
        else:
            produtos[id]['quantity'] = int(produtos[id]['quantity']) + 1

    elif 'removeItem' in request.args:
        id = request.args.get('removeItem')
        
        if id in produtos:
            produtos[id]['quantity'] = int(produtos[id]['quantity']) - 1
            if produtos[id]['quantity'] == 0:
                del produtos[id]

        print(produtos)

    carrinho['valorTotal'] = 0
    for key, produto in produtos.items():
        carrinho['valorTotal'] = int(carrinho['valorTotal']) + (int(produto['valor']) * int(produto['quantity']))
    
    
    carrinho['valorTotalComFrete'] = carrinho['valorTotal'] + 8

    session['myCarrinho'] = carrinho

    ##prod = Produtos.query.filter_by(id=2).first()
    return render_template("carrinho.html", carrinho=carrinho)

# PRODUTOS
@app.route("/produtos/")
def produtos():
    produtos = Produtos.query.all()
    return render_template("produtos.html", produtos=produtos)


# PEDIDOS
@app.route("/pedidos/")
def ped():
    return render_template("pedidos.html")


# LOGIN
@app.route("/login/", methods=["GET", "POST"])
def login():
    print(current_user.is_authenticated)
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['senha']

        user = Usuarios.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            # imprimit mensagem de erro
            return render_template('login.html', error='Usuário ou senha incorretos.')

        login_user(user, remember=True)
        flask.flash('Logged in successfully.')
        session['email'] = user.email
        return flask.redirect('/')

    return render_template('login.html')


# CADASTRO
@app.route("/cadastro/", methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        
        user = Usuarios.query.filter_by(email=email).first()
        if user:
            return render_template("cadastro.html", messageError="Usuário já existe!")

        senha = request.form["senha"]
        a = Usuarios(nome, email, senha)
        db.session.add(a)
        db.session.commit()
        return render_template("cadastro.html", message='Usuário cadastrado com sucesso. Realize o login')
    return render_template("cadastro.html")


@app.route("/sair/")
def logout():
    session.clear()
    logout_user()
    return flask.redirect('/login')
