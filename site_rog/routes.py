from flask import render_template, redirect,url_for, flash, request
from site_rog import app
from site_rog.forms import FormLogin,FormCriarConta



lista_usuarios=['rogerio','xico','pipoca']

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

