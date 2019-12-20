import os
import unittest
from ohipa import create_app, db


def clear_Db(self):
    self.db.drop_all()
    self.db.create_all()

def create_App_Test(self):
    app = create_app()
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQL_ALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(basedir,"test.db")
    self.app = app.test_client()
    self.db = db
    clear_Db(self)
