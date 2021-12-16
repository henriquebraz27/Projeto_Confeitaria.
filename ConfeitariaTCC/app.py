from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:mypass123@127.0.0.1:3306/confeitaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisissecret'
db = SQLAlchemy(app)

import models, routes

if __name__ == '__main__':
    app.run('0.0.0.0', 5433, debug=True)