#rodar e acessar pelo Firefox (ou chrome)
#se voce não conseguir rodar, talvez seja a falta da biblioteca.
#nesse caso, rode no CMD: pip install flask --user
#MAC ou Linux: pip3 install flask --user
 
from flask import Flask         #burocracia que vai ter sempre
from flask import jsonify 
from flask import request 


app = Flask(__name__)  



#@approute("",method)
def func():
    pass











if __name__ == '__main__':     #IF esse arquivo foi rodado direto,
                               # não foi chamado como biblioteca
   app.run(host = 'localhost', port = 5002, debug = True)
                               #suba um servidor, na porta 5002,
                               #configuração de debug
                               #debug: salvar dá reload
