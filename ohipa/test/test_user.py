import unittest, requests, os
import json
from ohipa import create_app
from ohipa.models import Users, db

new_user = {
    "mail_User":"tamatini@hotmail.fr",
    "nom_User": "teahui",
    "prenom_User": "tamatini",
    "password_User": "mahana"
}

user_url = 'http://localhost:5000/User/'


class UserServiceTest(unittest.TestCase):

    def createNewUser(self):
        self.app.post("/User/", json=new_user)

    def clearDb(self):
        self.db.drop_all()
        self.db.create_all()

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQL_ALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(basedir,"test.db")
        self.app = app.test_client()
        self.db = db
        self.clearDb()
        
    def test_return_users_view(self):
        response = self.app.get("/User/")
        self.assertEqual(response.status_code, 200)

    def test_post_new_user(self):
        response = self.app.post("/User/", json=new_user)
        self.assertEqual(response.json, "cet utilisateur à été créer")

    def test_return_all_user(self):       
        response = self.app.get("/User/")
        if self.assertEqual(response.json, [], "La liste est vide"):
            self.createNewUser()
            self.assertNotEqual(response.json, [], "la liste à été rempli")
        else:
            self.assertEqual(response.json, [], "La liste est vide")

    def test_return_list_of_user(self):
        self.createNewUser()
        response = self.app.get("/User/")
        response_list = response.json[0]
        response_test = response_list["nom_User"], response_list["prenom_User"], response_list["mail_User"]
        self.assertEqual(response_test, ("TEAHUI", "Tamatini", "tamatini@hotmail.fr"))
        
    def test_user_already_exist(self):
        self.createNewUser()
        response = self.app.post("/User/", json=new_user)
        self.assertEqual(response.json, "Cet utilisateur existe déjà")

    def test_update_user_password(self):
        self.app.post("/User/", json=new_user)
        new_password = {
            "mail_User": "tamatini@hotmail.fr",
            "password_User": "mahana",
            "new_Password": "tamatini"
        }
        response = self.app.put("/User/", json=new_password)
        self.assertEqual(response.json, "Mot de passe mis à jour")

    def test_user_delete(self):
        self.createNewUser()
        response = self.app.get("/User/")   
        delete_user = {
            "mail_User":"tamatini@hotmail.fr",
            "password_User": "mahana",
            "confirm_Password": "mahana"
        }
        response = self.app.delete("/User/", json=delete_user)
        self.assertEqual(response.json, "Compte supprimer")

if __name__ == '__main__':
    unittest.main()
    