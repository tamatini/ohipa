from ohipa.models import Commune, db, Ile
from flask_restplus import fields, Resource, Namespace
from flask import request, jsonify


api = Namespace('Communes', description="liste des communes")

new_commune = api.model('Commune', {
    'nom_commune': fields.String,
    'nom_ile': fields.String
})

@api.route("/")
class Commune_List(Resource):
    def get(self):
        return [{'Commune': c.commune_Nom.lower(), 'ile': c.ile_ID} for c in Commune.query.all()]

    @api.expect(new_commune)
    def post(self):
        nom_commune = request.json['nom_commune']
        nom_ile = request.json['nom_ile']
        iles = Ile.query.filter_by(ile_Nom=nom_ile.lower()).first()
        ile_ID = Ile.query.get(iles.ile_ID)
        if Commune.query.filter_by(commune_Nom=nom_commune.lower(), ile_ID=nom_ile.lower()).first():
            return jsonify('cette commune existe déjà')
        else:
            commune = Commune(commune_Nom=nom_commune.lower(), ile=ile_ID)
            db.session.add(commune)
            db.session.commit()
            return ('commune créer')