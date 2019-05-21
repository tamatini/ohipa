from ohipa.models import db, Categorie
from flask_restplus import fields, Namespace, Resource
from flask import request, jsonify


api = Namespace('Categorie', description='Liste des catégorie')


new_categorie = api.model('categorie', {
    'categorie_Nom': fields.String
})


@api.route('/')
class Categories(Resource):
    #Listing de toute les catégories
    def get(self):
        return [{'Categorie': c.categorie_Nom} for c in Categorie.query.all()]

    @api.expect(new_categorie)
    #Création d'une nouvelle catégorie
    def post(self):
        categorie_nom = request.json['categorie_Nom']
        #Vérifie si la catégorie n'est pas déjà créer
        if Categorie.query.filter_by(categorie_Nom=categorie_nom.lower()).first():
            return jsonify('cette catégorie existe déjà')
        else:
            #Commit la catégorie
            categorie = Categorie(categorie_Nom=categorie_nom.lower())
            db.session.add(categorie)
            db.session.commit()
            return jsonify('Catégorie créer')
