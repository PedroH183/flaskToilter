from flask import render_template
from app import app

@app.route('/home/<user>')
@app.route('/home', defaults = {'user':None})
def home(user):
    return render_template('home.html', user = user) # o flask vai buscar por padrão dentro dentro da pasta template

@app.route('/home/base/')
def perfil():
    return render_template('base.html')


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