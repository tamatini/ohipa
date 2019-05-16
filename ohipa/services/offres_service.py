from ohipa.models import db, Offres, Users, Commune, Ile, Categorie
from flask_restplus import fields, Resource, Namespace
from flask import request, jsonify

api = Namespace('Offres', description='Les offres')

new_offre = api.model('offre',{
    'categorie': fields.String,
    'ile': fields.String,
    'commune': fields.String,
    'detail': fields.String,
    'prix': fields.String,
    'user': fields.String
})

@api.route('/')
class Offre(Resource):
    def get(self):
        return [{'Offre': c.offre_Details} for c in Offres.query.all()]

    @api.expect(new_offre)
    def post(self):
        categorie = request.json['categorie']
        ile = request.json['ile']
        commune = request.json['commune']
        detail = request.json['detail']
        prix = request.json['prix']
        user = request.json['user']
        if Users.query.filter_by(username = user.lower()).first():
            username = Users.query.filter_by(username = user.lower()).first()
            user_ID = Users.query.get(username.user_ID)
            if Commune.query.filter_by(commune_Nom=commune.lower()).first():
                communes = Commune.query.filter_by(commune_Nom=commune.lower()).first()
                commune_ID = Commune.query.get(communes.commune_ID)
                if Ile.query.filter_by(ile_Nom=ile.lower()).first():
                    iles = Ile.query.filter_by(ile_Nom=ile.lower()).first()
                    ile_ID = Ile.query.get(iles.ile_ID)
                    if Categorie.query.filter_by(categorie_Nom=categorie.lower()).first():
                        categories = Categorie.query.filter_by(categorie_Nom=categorie.lower()).first()
                        categorie_ID = Categorie.query.get(categories.categorie_Id)
                        offre = Offres(offre_Details=detail, prix=prix, user_Id=user_ID,
                                       commune_Id=commune_ID, ile_Id=ile_ID, categorie_Id=categorie_ID)
                        db.session.add(offre)
                        db.session.commit()
                        return jsonify("Offre créer")
                    else:
                        return jsonify("cette catégorie n'existe pas")
                else:
                    return jsonify("cette ile n'existe pas")
            else:
                return jsonify("cette commune n'existe pas")
        else:
            return jsonify("cet utilisateur n'existe pas")