from flask_restplus import Api
from .users_service import api as user
from .login_service import api as login
from .iles_service import api as ile
from .commune_service import api as commune
from .offres_service import api as offre
from .categorie_service import api as categorie

api = Api(title="Ohipa na'ina'i API",
          version="1.0 alpha",
          description="API webservices Ohipa Na'ina'i")

api.add_namespace(user)
api.add_namespace(login)
api.add_namespace(ile)
api.add_namespace(commune)
api.add_namespace(offre)
api.add_namespace(categorie)