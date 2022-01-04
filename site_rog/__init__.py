from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b4ba0a4cf07b87991d1aec13cc70b7f0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

# agora precisa criar o banco de dados
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

from site_rog import routes
#tem de ser no final pois precisa do app pra funcionar
