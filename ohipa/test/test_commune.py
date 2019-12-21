import os
import unittest
from ohipa import create_app, db
from . import create_App_Test, clear_Db

expected_list = {'Commune': 'Mahina', 'ile': 'Tahiti'}


class CommuneServiceTest(unittest.TestCase):
    
    def setUp(self):
        create_App_Test(self)

    def test_return_commune_view(self):
        response = self.app.get('/Communes/')
        self.assertEqual(response.status_code, 200)

    def test_return_post_commune(self):
        self.app.post('/Iles/', json = {'nom_ile': 'tahiti'})
        self.app.post('/Communes/', json = {'nom_commune': 'mahina', 'nom_ile': 'tahiti'})
        response = self.app.get('/Communes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0], expected_list)

    def test_return_post_commune_case_responsive(self):
        self.app.post('/Iles/', json = {'nom_ile': 'taHitI'})
        self.app.post('/Communes/', json = {'nom_commune': 'maHINa', 'nom_ile': 'taHIti'})
        response = self.app.get('/Communes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0], expected_list)

if __name__ == '__main__':
    unittest.main()                                   