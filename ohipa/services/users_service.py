from flask_restplus import Namespace, Resource, fields
from ohipa.models import Users, db
from flask import request, jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
api = Namespace("User", description="Les utilisateurs")

new_user = api.model('User', {
    'user_Mail': fields.String,
    'nom_User': fields.String,
    'prenom_User': fields.String,
    'password_User': fields.String,
})

update_user = api.model('Update_User', {
    'user_Mail': fields.String,
    'password_User': fields.String,
    'new_Password': fields.String
})

delete_user = api.model('Delete_User', {
    'user_Mail': fields.String,
    'password_User': fields.String,
    'confirm_Password': fields.String
})

@api.route("/")
class UserList(Resource):

    def get(self):
        return [{'ID': c.user_ID, 'user_Mail': c.user_Mail} for c in Users.query.all()]

    @api.expect(new_user)  
    def post(self):
        mail = request.json['user_Mail']
        nom = request.json['nom_User']
        prenom = request.json['prenom_User']
        password = request.json['password_User']
        if Users.query.filter_by(user_Mail=mail).first():
            return jsonify('Cet utilisateur existe déjà')
        else:
            user = Users(user_Mail=mail, nom_User=nom, prenom_User=prenom)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()
            return  jsonify("cet utilisateur à été créer")

    @api.expect(update_user)
    def put(self):
        mail = request.json['user_Mail']
        password = request.json['password_User']
        new_Password = request.json['new_Password']
        user = Users.query.filter_by(user_Mail=mail).first()
        nom = user.nom_User
        prenom = user.prenom_User
        if not user or not user.verify_password(password):
            return jsonify("Vérifier le nom d'utilisateur ou le mot de passe")
        if password != new_Password:
            user_update = Users.query.get(user.user_ID)
            user_update.hash_password(new_Password)
            db.session.add(user_update)
            db.session.commit()
            return jsonify("Mot de passe mis à jour")
        else:
            return jsonify("Le mot de passe en identique, utilisez un autre mot de passe")

    @api.expect(delete_user)
    def delete(self):
        mail = request.json['user_Mail']
        password = request.json['password_User']
        confirm_password = request.json['confirm_Password']
        user = Users.query.filter_by(user_Mail=mail).first()
        if confirm_password!= password:
            return jsonify("Le mot de passe n'est pas identique, veuillez le saisir à nouveau")
        if not user or not user.verify_password(password):
            return jsonify("Vérifier le nom d'utilisateur ou le mot de passe")
        user_delete = user.query.get(user.user_ID)
        db.session.delete(user_delete)
        db.session.commit()
        return jsonify('Compte supprimer')