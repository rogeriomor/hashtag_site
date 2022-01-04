from flask import render_template, redirect, url_for, flash, request
from site_rog import app, database, bcrypt
from site_rog.forms import FormLogin, FormCriarConta
from site_rog.models import Usuario



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
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}','alert-success')
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript= bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso para o e-mail: {form_criarconta.email.data}','alert-success')
        return redirect(url_for('home'))
    return render_template('login_cc.html', form_login=form_login, form_criarconta=form_criarconta)

