from importlib.resources import path
import os

DEBUG = True # ativa o relod automatico

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'TaSeguro'
