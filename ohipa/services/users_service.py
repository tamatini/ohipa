from flask_restplus import Namespace, Resource, fields
from ohipa.models import Users, db
from flask import request, jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
api = Namespace("User", description="Les utilisateurs")

new_user = api.model('User', {
    'username': fields.String,
    'nom_User': fields.String,
    'prenom_User': fields.String,
    'password_User': fields.String
})

@api.route("/")
class UserList(Resource):
    def get(self):
        return [{'ID': c.user_ID, 'username': c.username, 'password': c.password_User} for c in Users.query.all()]

    @api.expect(new_user)
    def post(self):
        username = request.json['username']
        nom = request.json['nom_User']
        prenom = request.json['prenom_User']
        password = request.json['password_User']
        if Users.query.filter_by(username=username).first():
            return jsonify('Cet utilisateur existe déjà')
        else:
            user = Users(username=username, nom_User=nom, prenom_User=prenom)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()
            return  jsonify("cet utilisateur à été créer")


