# a pasta templates tem de ter exatamente este nome pois o flask vai procurar por ela para interligar as pastas, e este é um padrão


from flask import Flask, render_template, url_for, request, flash, redirect
# essa importação do request tem o botaosubmit login
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy


'''esse url_for serve pra padronizar o acesso, 
e se precisar mudar o link muda tudo de uma vez, 
pois vai mudar o link dentro da função, so nao pode mudar o nome da função'''

app = Flask(__name__)  # isso aqui sempre precis ter

lista_usuarios=['rogerio','xico','pipoca']
'''pra nao gerar esse token na mao, 
usando o terminal pode-se importar a biblioteca secrets e 
da o comandosecrets.token_hex(16 e ele cria um token seguro de 16 bytes'''

app.config['SECRET_KEY'] = 'b4ba0a4cf07b87991d1aec13cc70b7f0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
''' esse sqlite e essas tres barras cria esse banco de dados, nesse caso mesmo local arquivo main'''

# agora precisa criar o banco de dados
database= SQLAlchemy(app)


@app.route('/')  # esse barra é o caminho da pasta
def home():
    return render_template('home.html')


@app.route('/insight')
def insight():
    return render_template('insight.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html',lista_usuarios=lista_usuarios)

@app.route('/login_cc', methods=['GET','POST'])
def login_cc():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form :
        #fez login com sucesso
        # aqui queremos exibir mensagem que login foi bem sucedido
        # redirecionar pra pagina inicial
        #pra fazer essas duas coisas acima precisa importar dois metodos, um pra cada,
        #flash pra exibir mensagens de alerta e
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}','alert-success')
        # redirect pra redirecionar
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        # criou conta com sucesso
        # quando vc clica no submit ele vai validar todos, pra separar, coloca-s o nome do botao, pois senao aperatndo um botao ele valida os dois e da confusao, isso aocntece pois tem dois botoes no mesmo questionario
        flash(f'Conta criada com sucesso para o e-mail: {form_criarconta.email.data}','alert-success')
        return redirect(url_for('home'))
    return render_template('login_cc.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)# esse debug=True garante que o site seja atualizado conforme muda o codigo

