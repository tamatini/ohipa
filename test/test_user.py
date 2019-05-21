import unittest
from ohipa.services.users_service import UserList
from unittest.mock import Mock, patch

def user(username, nom_User, prenom_User):
    user = Mock()
    user.username = username
    user.nom_User = nom_User
    user.prenom_User = prenom_User
    return user

class TestUser(unittest.TestCase):

    new_user = [{
        'username': 'Tamatini',
        'nom_User': 'TEAHUI',
        'prenom_User': 'Tamatini',
    }]

    @patch('ohipa.services.users_service.UserList')
    def test_post(self, user_mock):
        user_mock.query.all.return_value = [user(u['username'], u['nom_User'], u['prenom_User']) for u in self.new_user]
        post = UserList()
        self.assertEqual(post, self.new_user)

