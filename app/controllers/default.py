from flask import flash, redirect, render_template, redirect, url_for
from app import app,lm
from flask_login import login_user,logout_user

from app.models.forms import LoginForm
from app.models.tables import User

@lm.user_loader
def load_user(id):
        return User.query.filter_by(id = id).first()

@app.route('/signup/', methods = ["Get","Post"])
def signup():
    form = 


@app.route('/login/', methods = ["Get","Post"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():

        user_lo = User.query.filter_by(username = form.username.data.title()).first()

        if user_lo and (user_lo.password == form.password.data):
            login_user(user_lo)
            flash("Logged in ")
            return redirect(url_for("home"))   # home é o nome da função 
        else:
            flash("Invalid Login")
    else:
        print(form.errors)

    return render_template('login.html', form = form) # o flask vai buscar por padrão dentro dentro da pasta template


@app.route('/home/<nome>')
@app.route('/home/', defaults = {'nome' : None}, methods = ["GET"])
def home(nome): # primeira operação é a operação 
    
    if nome is not None:
        data = User.query.filter_by(username = nome.title() ).first()
        return render_template('home.html', users = data.username.title() )
    else:
        data = User.query.filter_by(username = "").first()
        return render_template('home.html', users = "")

@app.route("/logout")
def loggout():
    logout_user()
    return redirect(url_for("login"))


# data = User.query.filter_by(campo = value ).first()
# db.session.delete(data) # para apagar um valor 
# data.campo = value ... db.session.commit(data) # para fazer a atualização de um valor
# db.session.add(data) .. db.session.commit(data) # para adicionar um valor ao DB 

# se a query não encontra valores correspondentes ele retorna None.
# query.all() return all values storaged in DB