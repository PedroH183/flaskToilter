from flask import render_template
from app import app
from app.models.forms import LoginForm


@app.route('/home/')
def tentando():
    return render_template('home.html')


@app.route('/login/', methods = ["Get","Post"])
def home():
    form = LoginForm()
    
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)

    return render_template('login.html', form = form) # o flask vai buscar por padrão dentro dentro da pasta template


"""
@app.route("/home", defaults = {'name':None}, methods = ['GET'])
@app.route('/home/<name>')
def test(name = None):
    if name:
        return "Olá meu nobre alcunhado como <b> %s <b>" % name.title()
    else:
        return "Olá anonimo user !"

@app.route("/home/<int:id>")
def teste(id = 0):
    if id:
        return "Olá user de id %d !" % id
    else:
        return "Olá user sem id ! "
"""