from flask_restplus import Resource, Namespace, fields
from ohipa.models import Users
from flask_httpauth import HTTPBasicAuth
from flask import request

auth = HTTPBasicAuth()
api = Namespace('Login', description= 'Test de la méthode de login')
credential = api.model('user', {
    'username': fields.String,
    'password': fields.String
})

@api.route('/')
class login(Resource):

    @auth.verify_password
    @api.expect(credential)
    def post(self):
        username = request.json['username']
        password = request.json['password']
        user = Users.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            return False
        return True