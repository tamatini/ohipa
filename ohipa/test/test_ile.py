import unittest
from ohipa.models import Ile, db
from . import create_App_Test, clear_Db
import os

expected_ile = [
    {'ile': 'Tahiti'},
    {'ile': 'Moorea'}
]

new_list = [
    {'nom_ile': 'Tahiti'},
    {'nom_ile': 'Moorea'}
]

class IleServiceTests(unittest.TestCase):

    def createIsland(self):
        self.app.post('/Iles/', json={'nom_ile': 'Tahiti'})
        self.app.post('/Iles/', json={'nom_ile': 'Moorea'})

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

if __name__ == '__main__':
    unittest.main()
    