import unittest
import requests
import json
from ohipa import create_app, db

class ViewsTest(unittest.TestCase):

    def test_home_Views(self):
        response = requests.get('/')
        self.assertEqual(response.status_code, 200)

    def test_return_communes_view(self):
        response = requests.get('/Communes/')
        self.assertEqual(response.status_code, 200)

    def test_return_offre_view(self):
        response = requests.get("/Offre/")
        self.assertEqual(response.status_code, 200)

    def test_return_categories_view(self):
        response = requests.get("/Categorie/")
        self.assertEqual(response.status_code, 200)


class IleTest(unittest.TestCase):

    def test_return_iles_view(self):
        response = requests.get(url='http://localhost:5000/Iles/')
        self.assertEqual(response.status_code, 200)

    def test_post_ile(self):
        response = requests.post(url='http://localhost:5000/Iles/', json={"nom_ile": "Tahiti"})
        self.assertEqual(response.json(), "Ile créer")

    def test_return_list_of_ile(self):
        response = requests.get(url="http://localhost:5000/Iles/")
        response_dict = json.loads(response.content.decode('utf-8'))
        response_list = response_dict[0]
        response_test = response_list["ile"]
        self.assertEqual(response_test, "Tahiti")

    def test_delete_ile(self):
        response = requests.delete(url="http://localhost:5000/Iles/", json={"nom_ile": "Tahiti"})
        self.assertEqual(response.json(), "Ile supprimer")   

if __name__ == '__main__':
    unittest.main()
    