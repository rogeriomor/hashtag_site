# a pasta templates tem de ter exatamente este nome pois o flask vai procurar por ela para interligar as pastas, e este é um padrão


from flask import Flask
# essa importação do request tem o botaosubmit login

from flask_sqlalchemy import SQLAlchemy

'''esse url_for serve pra padronizar o acesso, 
e se precisar mudar o link muda tudo de uma vez, 
pois vai mudar o link dentro da função, so nao pode mudar o nome da função'''

app = Flask(__name__)  # isso aqui sempre precis ter


'''pra nao gerar esse token na mao, 
usando o terminal pode-se importar a biblioteca secrets e 
da o comandosecrets.token_hex(16 e ele cria um token seguro de 16 bytes'''

app.config['SECRET_KEY'] = 'b4ba0a4cf07b87991d1aec13cc70b7f0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
''' esse sqlite e essas tres barras cria esse banco de dados, nesse caso mesmo local arquivo main'''

# agora precisa criar o banco de dados
database= SQLAlchemy(app)

from site_rog import routes #tem de ser no final pois precisa do app pra funcionar
