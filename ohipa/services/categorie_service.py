from ohipa.models import db, Categorie
from flask_restplus import fields, Namespace, Resource
from flask import request, jsonify


api = Namespace('Categorie', description='liste des catégories de travail')

new_categorie = api.model('categorie', {
    'categorie_Nom': fields.String
})

@api.route('/')
class Categorie(Resource):
    def get(self):
        return [{'Categorie': c.categorie_Nom} for c in Categorie.query.all()]

    @api.expect(new_categorie)
    def post(self):
        categorie_Nom = request.json['categorie_Nom']
        if Categorie.query.filter_by(categorie_Nom=categorie_Nom.lower()).first():
            return jsonify('cette catégorie existe déjà')
        else:
            categorie = Categorie(categorie_Nom=categorie_Nom.lower())
            db.session.add(categorie)
            db.session.commit()
            return jsonify('Catégorie créer')
