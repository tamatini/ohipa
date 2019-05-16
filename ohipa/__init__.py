from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
SECRET_KEY = "b'\xf8\xc2)\xb6\r\xaf\xdcz\x99\xc6\xeeu\xa3J\x1c\x1e\xb1\xe2h\xd5\x07\xe5\x9e\xbfd>jjC\r\x99\r'"

def create_app(config_file=None):
    app= Flask(__name__)
    if config_file:
        app.config.from_pyfile(config_file)
    else:
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    from .services import api
    api.init_app(app)
    app.app_context().push()
    db.create_all(app=app)
    return app