import unittest
from flask import Flask
import requests
import json
from ohipa.models import Users

new_user = {
    "mail_User":"tamatini@hotmail.fr",
    "nom_User": "teahui",
    "prenom_User": "tamatini",
    "password_User": "mahana"
}

user_url = 'http://localhost:5000/User/'

class ViewsTest(unittest.TestCase):

    def test_home_Views(self):
        response = requests.get(url='http://localhost:5000')
        self.assertEqual(response.status_code, 200)

    def test_return_iles_view(self):
        response = requests.get(url='http://localhost:5000/Iles/')
        self.assertEqual(response.status_code, 200)

    def test_return_communes_view(self):
        response = requests.get(url="http://localhost:5000/Communes/")
        self.assertEqual(response.status_code, 200)

    def test_return_offre_view(self):
        response = requests.get(url="http://localhost:5000/Offres/")
        self.assertEqual(response.status_code, 200)

    def test_return_categories_view(self):
        response = requests.get(url="http://localhost:5000/Categorie/")
        self.assertEqual(response.status_code, 200)

class UserServiceTest(unittest.TestCase):

    def test_return_users_view(self):
        response = requests.get(url=user_url)
        self.assertEqual(response.status_code, 200)


    def test_post_new_user(self):
        response = requests.post(url=user_url, json=new_user)
        self.assertEqual(response.json(), "cet utilisateur à été créer")


    def test_user_already_exist(self):
        response = requests.post(url=user_url, json=new_user)
        self.assertEqual(response.json(), "Cet utilisateur existe déjà")

    def test_update_user_password(self):
        new_password = {
            "mail_User": "tamatini@hotmail.fr",
            "password_User": "mahana",
            "new_Password": "tamatini"
        }

        response = requests.put(url=user_url, json=new_password)
        self.assertEqual(response.json(), "Mot de passe mis à jour")


    def test_user_delete(self):
        delete_user = {
            "mail_User":"tamatini@hotmail.fr",
            "password_User": "tamatini",
            "confirm_Password": "tamatini"
        }

        response = requests.delete(url=user_url, json=delete_user)
        self.assertEqual(response.json(), "Compte supprimer")


if __name__ == '__main__':
    unittest.main()
    