import unittest
from ohipa.models import Ile, db
from . import create_App_Test, clear_Db
import os

expected_ile = [
    {'ile': 'Tahiti', 'communes': []},
    {'ile': 'Moorea', 'communes': []}
]

new_list = [
    {'nom_ile': 'Tahiti'},
    {'nom_ile': 'Moorea'}
]

class IleServiceTests(unittest.TestCase):

    def createIsland(self):
        self.app.post('/Iles/', json={'nom_ile': 'Tahiti'})
        self.app.post('/Iles/', json={'nom_ile': 'Moorea'})

    def createCommune(self):
        self.app.post('/Communes/', json={'nom_commune': 'Mahina', 'iles': 'Tahiti'})
        self.app.post('/Communes/', json={'nom_commune': 'Papenoo', 'iles': 'Tahiti'})
        self.app.post('/Communes/', json={'nom_commune': 'Papeete', 'iles': 'Tahiti'})
        self.app.post('/Communes/', json={'nom_commune': 'Temae', 'iles': 'Moorea'})
        self.app.post('/Communes/', json={'nom_commune': 'Paopao', 'iles': 'Moorea'})
        self.app.post('/Communes/', json={'nom_commune': 'Afaraitu', 'iles': 'Moorea'})

    def setUp(self):
        create_App_Test(self)

    def test_post_new_ile(self):
        response = self.app.post('/Iles/', json={'nom_ile':'Tahiti'})
        self.assertEqual(response.json, 'Ile créer')

    def test_return_ile_view(self):
        response = self.app.get('/Iles/')
        self.assertEqual(response.status_code, 200)

    def test_return_ile_list(self):
        self.createIsland()
        response = self.app.get('/Iles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_ile)

    def test_return_all_ile(self):
        self.createIsland()
        response = self.app.get('/Iles/')
        self.assertEqual(len(response.json), len(expected_ile))

    def test_delete_one_ile(self):
        self.createIsland()
        response = self.app.delete('/Iles/', json={'nom_ile': 'Tahiti'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, "Ile supprimer")
        response = self.app.get('/Iles/')
        self.assertEqual(len(response.json), 1)

    def test_return_list_of_communes_per_island(self):
        self.createIsland()
        self.createCommune()
        response = self.app.get('/Iles/')
        print(response.json)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json, expected_ile)

if __name__ == '__main__':
    unittest.main()
    