# pra gerenciar formularios no flask precisa instalar um arquivo do flask, que seria o flask-wtf, pra dentor do ambeinte virtual

from flask_wtf import FlaskForm  # obervar que na hora de importar é com underline
#campos de texto, de senha de botao, vem da classe WTForms que foi instalada junto, dai precisa importa-la
from wtforms import StringField, PasswordField, SubmitField
# para que existam validações dos campos que estao sendo preenchidos, precisa importar uma bibliotec chamada validators
from wtforms.validators import DataRequired, Length, Email,EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuario', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confirmação de senha', validators=[DataRequired(),EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    senha = PasswordField('senha',validators=[DataRequired(),Length(6,20)])
    botao_submit_login = SubmitField('Fazer Login')# nao pode ter o memso nome do anterior pois os dois botoes estarão na mesma pagina, sendo assim precisam ter nomes diferentes

    #csrf token # esse treco protge o formulario contra ataques externos