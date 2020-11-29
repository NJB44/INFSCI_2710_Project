import os
from flask import Flask 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SIJAX_STATIC_PATH = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
    SIJAX_JSON_URI = '/static/js/sijax/json2.js'
    BOOTSTRAP_BOOTSWATCH_THEME = 'lux'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:5Qf*6*oD@localhost/SmartPharm'
    SQLALCHELMY_TRACK_MODIFICATIONS = False
