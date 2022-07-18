from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' # URI de conexão com o DB

db = SQLAlchemy(app) 

migrate = Migrate(app,db) # vai gerenciar as migrações 

from app.controllers import default