from flask import render_template
from app import app,db

from app.models.forms import LoginForm
from app.models.tables import User

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

@app.route('/teste/<info>')
@app.route('/teste/', defaults = {'info':None} )
def teste(info): # primeira operação é a operação 
    red = User.query.filter_by(name = "pedro henrique").all()
    print(red)
    return "Ok"

