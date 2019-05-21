from ohipa.models import Commune, db, Ile
from flask_restplus import fields, Resource, Namespace
from flask import request, jsonify


api = Namespace('Communes', description="Liste des communes")

#Champ de données
new_commune = api.model('Commune', {
    'nom_commune': fields.String,
    'nom_ile': fields.String
})

@api.route("/")
class Commune_List(Resource):
    #Listing des Communes
    def get(self):
        return [{'Commune': c.commune_Nom.lower(), 'ile': c.ile_ID} for c in Commune.query.all()]

    @api.expect(new_commune)
    #Méthode de création des communes
    def post(self):
        nom_commune = request.json['nom_commune']
        nom_ile = request.json['nom_ile']
        iles = Ile.query.filter_by(ile_Nom=nom_ile.lower()).first() #Récupère l'ID de l'ile
        ile_ID = Ile.query.get(iles.ile_ID)
        if Ile.query.filter_by(ile_ID=ile_ID): #Vérifie que l'ile existe avec l'ID
            if Commune.query.filter_by(commune_Nom=nom_commune.lower()).first(): #Vérifie que la commune n'est pas créer
                return jsonify('Cette commune existe déjà')
            else:
                commune = Commune(commune_Nom=nom_commune.lower(), ile=ile_ID)
                db.session.add(commune)
                db.session.commit()
                return ('La commune à été créer')
        else:
            return jsonify("Cette île n'existe pas")