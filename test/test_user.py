import unittest
import requests
import json

new_user = {
    "mail_User":"tamatini@hotmail.fr",
    "nom_User": "teahui",
    "prenom_User": "tamatini",
    "password_User": "mahana"
}


user_url = 'http://localhost:5000/User/'


class UserServiceTest(unittest.TestCase):
    
    def test_return_users_view(self):
        response = requests.get(url=user_url)
        self.assertEqual(response.status_code, 200)

    def test_post_new_user(self):
        response = requests.post(url=user_url, json=new_user)
        self.assertEqual(response.json(), "cet utilisateur à été créer")

    def test_return_list_of_user(self):
        response = requests.get(url=user_url)
        response_dict = json.loads(response.content.decode('utf-8'))
        response_list = response_dict[0]
        response_test = response_list["nom_User"], response_list["prenom_User"], response_list["mail_User"]
        self.assertEqual(response_test, ("TEAHUI", "Tamatini", "tamatini@hotmail.fr"))
        
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
    