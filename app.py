from flask import Flask, render_template, request, flash
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Usuario
app.config['SECRET_KEY'] = '23ttnd4gnd55y-23md98'

# drive://usuario:senha@servidor/bancodedados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/law"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aula')
@app.route('/aula/<nome>')
@app.route('/aula/<nome>/<curso>')
@app.route('/aula/<nome>/<curso>/<int:ano>')
def aula(nome = 'João', curso = 'Informática', ano = 1):
    dados = {'nome':nome,'curso':curso, 'ano':ano}
    return render_template('aula.html',dados_curso = dados)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados', methods=['POST'])
def dados():
    flash('Dados ')
    dados = request.form
    return render_template('dados.html', dados=dados)

if __name__ == '__main__':
    app.run()

@app.route('/usuario')
def usuario():
    u = Usuario.query.al()   #selec usuario from (nome da tabela)
    return render_template('usuario_lista.html', dados = u)

