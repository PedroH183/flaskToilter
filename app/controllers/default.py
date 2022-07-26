from flask import flash, redirect, render_template, redirect, url_for
from app import app,lm,db
from flask_login import login_user,logout_user

from app.models.forms import LoginForm, SignupForm
from app.models.tables import User

@lm.user_loader
def load_user(id):
        return User.query.filter_by(id = id).first()


@app.route('/signup/', methods = ["Get","Post"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        user_nm = User.query.filter_by(username = form.username.data).first()
        email_nm = User.query.filter_by(email = form.email.data).first()

        if (not user_nm and not email_nm):
            # possible erro of integritary 

            sign_valid = User(form.username.data,form.password.data,form.name.data,form.email.data)
            db.session.add(sign_valid)
            db.session.commit()
            return redirect(url_for("home"))

        else:
            flash("Repeted information")
    else:
        print(form.errors)

    return render_template("signup.html", form=form)


@app.route('/login/', methods = ["Get","Post"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():

        user_lo = User.query.filter_by(username = form.username.data).first()

        if user_lo and (user_lo.password == form.password.data):
            login_user(user_lo)
            flash("Logged in ")
            return redirect(url_for("home"))   # home é o nome da função 
        else:
            flash("Invalid Login")
    else:
        print(form.errors)

    return render_template('login.html', form = form) # o flask vai buscar por padrão dentro dentro da pasta template


@app.route('/home/', methods = ["GET"])
def home(): # primeira operação é a operação 
    return render_template('home.html')

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