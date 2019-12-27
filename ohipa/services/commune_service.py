from ohipa.models import Commune, db, Ile
from flask_restplus import fields, Resource, Namespace
from flask import request, jsonify


api = Namespace('Communes', description="Liste des communes")

#Champ de données
new_commune = api.model('Commune', {
    'nom_commune': fields.String,
    'iles': fields.String
})

@api.route("/")
class Commune_List(Resource):
    #Listing des Communes
    def get(self):
        return [{'Commune': c.commune_Nom.capitalize(), 'ile_ID': c.ile_ID.capitalize()} for c in Commune.query.all()]

    @api.expect(new_commune)
    #Méthode de création des communes
    def post(self):
        nom_commune = request.json['nom_commune']
        nom_ile = request.json['iles']
        commune = Commune(commune_Nom=nom_commune, ile_ID=nom_ile)
        db.session.add(commune)
        db.session.commit()