# a pasta templates tem de ter exatamente este nome pois o flask vai procurar por ela para interligar as pastas, e este é um padrão


from flask import Flask, render_template

app = Flask(__name__)# isso aqui sempre precis ter

@app.route('/') # esse barra é o caminho da pasta
def home():
    return render_template('home.html')


@app.route('/insight')
def insight():
    return render_template('insight.html')

if __name__ == '__main__':
    app.run(debug=True)

    print()