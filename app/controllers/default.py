from flask import render_template
from app import app,db

from app.models.forms import LoginForm
from app.models.tables import User

@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/login/', methods = ["Get","Post"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)

    return render_template('login.html', form = form) # o flask vai buscar por padrão dentro dentro da pasta template


@app.route('/teste/<nome>')
@app.route('/teste/', defaults = {'nome' : None})
def teste(nome): # primeira operação é a operação 
    
    if nome is not None:
        data = User.query.filter_by(username = nome.title()).first()
    else:
        data = User.query.filter_by(username = "").first()

    if data is not None:
        return render_template('home.html', users = data.username.title() )
    else: 
        return render_template('home.html', users = "")

# data = User.query.filter_by(campo = value ).first()
# db.session.delete(data) # para apagar um valor 
# data.campo = value ... db.session.commit(data) # para fazer a atualização de um valor
# db.session.add(data) .. db.session.commit(data) # para adicionar um valor ao DB 

# se a query não encontra valores correspondentes ele retorna None.
# query.all() return all values storaged in DB