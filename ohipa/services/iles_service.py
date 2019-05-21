from ohipa.models import Ile, Commune
from flask_restplus import Namespace, fields, Resource
from flask import request, jsonify
from ohipa import db

api = Namespace('Iles', description='Liste des Iles')

# Champ de données
ile = api.model('ile', {
    'nom_ile': fields.String
})


@api.route('/')
class Iles(Resource):
    # Retourne la liste des îles
    def get(self):
        return [{'ile': c.ile_Nom.capitalize()} for c in Ile.query.all()]

    @api.expect(ile)
    def post(self):
        # Méthode de création d'une île
        ile = request.json['nom_ile']
        if Ile.query.filter_by(ile_Nom=ile.lower()).first(): # Vérifie si l'île n'est pas créer
            return jsonify('Ile déjà enregistré')
        else:
            new_ile = Ile(ile_Nom=ile.lower()) # Commit la nouvelle île
            db.session.add(new_ile)
            db.session.commit()
            return jsonify('Ile créer')

    """
    @api.expect(ile)
    def delete(self):
        ile = request.json['nom_ile']
        if Ile.query.filter_by(ile_Nom=ile.lower()).first(): # Vérifie si l'île existe
            iles = Ile.query.filter_by(ile_Nom=ile.lower()).first()
            delete_ile = iles.query.get(iles.ile_ID) # Récupère l'ID de l'île
            db.session.delete(delete_ile) # commit la suppression
            db.session.commit()
            return jsonify('Ile supprimmer')
        else:
            return jsonify("cette îles n'est pas dans la liste")
    """

@api.route('/commune')
class commune(Resource):
    # Retourne la liste des communes en fonction de l'île
    @api.expect(ile)
    def post(self):
        nom_ile = request.json['nom_ile']
        # Vérifie l'île et récupère l'ID
        iles = Ile.query.filter_by(ile_Nom=nom_ile.lower()).first()
        ile_ID = Ile.query.get(iles.ile_ID)
        # Retourne la liste
        return [{'commune': c.commune_Nom.capitalize()} for c in Commune.query.filter_by(ile=ile_ID)]