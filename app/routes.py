from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html' ,titulo = 'pagina inicial')


@app.route('/contatos')
def contatos():
    return render_template('contatos.html' , titulo = 'contatos')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html' , titulo = 'sobre')


@app.route('/projetos')
def projetos():
    return render_template('projetos.html' , titulo = 'projetos')