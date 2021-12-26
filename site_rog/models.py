
from site_rog import database  #este database é usado pelo sqlalchemy
from datetime import datetime

# por que models?, é porque os modelos e tabelas costuma-se usar models.py tabelas configuração do que o bco de dados vai armazenar
class Usuario(database.Model):
    # essa classe vai receber tudo, vai herdar,
    # vai ser uma subclasse de uma classe padrao de um bco de dados so vai precisar definir as colunas
    # ideal é usar o mesmo nome dos formularios se usar nome diferente pode gerar duvias e erros

    id=database.Column(database.Integer, primary_key=True)
    username=database.Column(database.String, nullable=False)
    email= database.Column(database.String, nullable=False, unique=True)
    senha=database.Column(database.String, nullable=False)
    foto_perfil= database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='não informado')

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable= False)
    corpo = database.Column(database.Text, nullable= False) # como o campo vai ser grande (varios paragrafos) nao coloca string e sim text, String so pra texto pequeno
    data_criacao= database.Column(database.DateTime, nullable=False, default= datetime.utcnow)
    # aqui tem de passar a função -sem () pois senao vai a data de agora, tem de colocar a função pra ele atuualizar
    # default, o padrao nao pode ser a data fixa
    # tambem nao pode colocar
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable = False)
    # a classe deve estar em letra minuscula
    #database.ForeignKey precisa ser o segundo argumento



