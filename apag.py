from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123@sql'
db=SQLAlchemy(app)


class usuarioo(db.Model):
    _tablename_ = 'userss'
    idconta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email=db.Column(db.String(550)) 
    senha = db.Column(db.String(20))
    def _init_(self, email,senha):
        self.email=email
        self.senha=senha
        
db.create_all()


@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        email=(request.form.get("e-mail"))
        senha= (request.form.get("s-enha"))
        if email:
             a = usuarioo(email,senha)
             db.session.add(a)
             db.session.commit()
    return redirect(url_for("index.html"))




if __name__ == "__main__":
    app.run(debug=True)