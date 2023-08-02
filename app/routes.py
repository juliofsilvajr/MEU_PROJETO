from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html'titulo = 'pagina inicial')


@app.route('/projetos')
def projetos():
    return render_template('projetos.html'titulo = 'projetos')