#rodar e acessar pelo Firefox (ou chrome)
#se voce não conseguir rodar, talvez seja a falta da biblioteca.
#nesse caso, rode no CMD: pip install flask --user
#MAC ou Linux: pip3 install flask --user

from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask




app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/confeitaria'
db=SQLAlchemy(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pedidos.html")   
def ped():
    return render_template("pedidos.html")


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = usuarios.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return render_template('login.html')       

        return render_template('home.html')

    return render_template('login.html')

class usuarios(db.Model):
    _tablename_ = 'userss'
    idconta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email=db.Column(db.String(550)) 
    senha = db.Column(db.String(20))
    def __init__(self,email,senha):
        self.email=email
        self.senha=(senha)

    def verify_password(self, pwd):
        return (self.senha, pwd)
        
db.create_all()


@app.route("/registro.html", methods=["GET","POST"])
def cadastrar():
    if request.method == "POST":
        email=request.form["txtemail"]
        senha=request.form["txtsenha"]
        a = usuarios(email,senha)
        db.session.add(a)
        db.session.commit()
    return render_template("registro.html")





"""
if __name__ == '__main__':     #IF esse arquivo foi rodado direto,
                               # não foi chamado como biblioteca
   app.run(host = 'localhost', port = 5002, debug = True)
                               #suba um servidor, na porta 5002,
                               #configuração de debug
                               #debug: salvar dá reload
"""

if __name__ == "__main__":
    
    app.run(debug=True)