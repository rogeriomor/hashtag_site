# a pasta templates tem de ter exatamente este nome pois o flask vai procurar por ela para interligar as pastas, e este é um padrão


from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta


#esse url_for serve pra padronizar o acesso, e se precisar mudar o link muda tudo de uma vez, pois vai mudar o link dentro da função, so nao pode mudar o nome da função
app = Flask(__name__)# isso aqui sempre precis ter

lista_usuarios=['rogerio','xico','pipoca']
#pra nao gerar esse token na mao, usando o terminal podese importar a biblioteca secrets e da o comandosecrets.token_hex(16 e ele cria um token seguro de 16 bytes
app.config['SECRET_KEY']='b4ba0a4cf07b87991d1aec13cc70b7f0'

@app.route('/') # esse barra é o caminho da pasta
def home():
    return render_template('home.html')


@app.route('/insight')
def insight():
    return render_template('insight.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html',lista_usuarios=lista_usuarios)

@app.route('/login_cc')
def login_cc():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login_cc.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)# esse debug=True garante que o site seja atualizado conforme muda o codigo

