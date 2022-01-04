from flask import render_template, redirect, url_for, flash, request
from site_rog import app, database, bcrypt
from site_rog.forms import FormLogin, FormCriarConta
from site_rog.models import Usuario
from flask_login import login_user, logout_user, current_user



lista_usuarios=['rogerio','xico','pipoca']

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/insight')
def insight():
    return render_template('insight.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login_cc', methods=['GET','POST'])
def login_cc():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}','alert-success')
            return redirect(url_for('home'))
        else:
            flash(f'Falha no login. Email ou Senha incorretos', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript= bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso para o e-mail: {form_criarconta.email.data}','alert-success')
        return redirect(url_for('home'))
    return render_template('login_cc.html', form_login=form_login, form_criarconta=form_criarconta)
@app.route('/sair')
def sair():
    logout_user()
    flash(f'Logout feito com sucesso', 'alert-success')
    return redirect(url_for('home'))

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/post/criar')
def criar_post():
    return render_template('criarpost.html')



