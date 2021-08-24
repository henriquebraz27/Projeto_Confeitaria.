#rodar e acessar pelo Firefox (ou chrome)
#se voce não conseguir rodar, talvez seja a falta da biblioteca.
#nesse caso, rode no CMD: pip install flask --user
#MAC ou Linux: pip3 install flask --user
 
from flask import Flask
from flask import render_template


app = Flask(__name__)  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login.html")   
def loggon():
    return render_template("login.html")

@app.route("/pedidos.html")   
def ped():
    return render_template("pedidos.html")






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