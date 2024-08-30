from flask import Flask, render_template, request, flash, redirect
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

@app.route('/usuario')
def usuario():
    u = Usuario.query.all()   #selec usuario from (nome da tabela)
    return render_template('usuario_lista.html', dados = u)

@app.route('/usuario/add')
def usuario_add():
    return render_template('usuario_add.html')

@app.route('/usuario/save', methods=['POST'])
def usuario_save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')
    if nome and email and idade:
        usuario = Usuario(nome, email, idade)
        db.session.add(usuario)
        db.session.commit()
        flash('usuário cadastrado com sucesso!!!')
        return redirect('/usuario')
    else:
        flash('Preencha todos os campos!!!')


    
if __name__ == '__main__':
    app.run()