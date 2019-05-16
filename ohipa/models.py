from . import db
from sqlalchemy import Column, Integer, String, ForeignKey
from passlib.apps import custom_app_context as pwd_context

class Users(db.Model):
    db.__tablename__ = "Users"
    db.__mapper__ = {"column_prefix": "Users"}
    user_ID = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(30), nullable=False, unique=True)
    nom_User = Column(String(30), nullable=False, unique=False)
    prenom_User = Column(String(30), nullable=False, unique=False)
    password_User = Column(String(128), nullable=False)
    Offres = db.relationship('Offres', backref='offres')

    def hash_password(self, password):
        self.password_User = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_User)

    def __repr__(self):
        return f"Users('{self.user_ID}', '{self.nom_User}', '{self.prenom_User}', '{self.username}', '{self.Offres}')"

class Offres(db.Model):
    db.__tablename__= "Offres"
    db.__mapper__= {"column_prefix": "Offres"}
    offre_ID = Column(Integer, primary_key=True, nullable=False)
    offre_Details = Column(String(200), nullable=False)
    prix = Column(String(30), nullable=False)
    user_Id = Column(Integer, ForeignKey("users.user_ID"))
    categorie_Id = Column(Integer, ForeignKey("categorie.categorie_Id"))
    commune_Id = Column(Integer, ForeignKey("commune.commune_ID"))
    ile_Id = Column(Integer, ForeignKey("ile.ile_ID"))

    def __repr__(self):
        return f"Offres('{self.offre_ID}', '{self.offre_Details}', '{self.Categories}', '{self.user_Id}')," \
            f"'{self.commune_Id}', '{self.ile_Id}'"


class Categorie(db.Model):
    db.__tablename__="Categorie"
    db.__mapper__= {"column_prefix": "Categorie"}
    categorie_Id = Column(Integer, nullable=False, primary_key=True)
    categorie_Nom = Column(String(20), nullable=False)
    Offres = db.relationship('Offres', backref='Categorie')

    def __repr__(self):
        return f"Categories('{self.categories_Id}','{self.categories_Name}', '{self.offre}')"

class Commune(db.Model):
    db.__tablename__ = "Commune"
    db.__mapper__ = {"column_prefix": "Commune"}
    commune_ID = Column(Integer, nullable=False, primary_key=True)
    commune_Nom = Column(String(30), nullable=False)
    ile_ID = Column(Integer, ForeignKey('ile.ile_ID'))
    Offres = db.relationship('Offres', backref='Commune')

    def __repr__(self):
        return f"Commune('{self.commune_ID}', '{self.commune_Nom}')"

class Ile(db.Model):
    db.__tablename__ = "Ile"
    db.__mapper_ = {"column_prefix": "Ile"}
    ile_ID = Column(Integer, nullable=False, primary_key=True)
    ile_Nom = Column(String(30), nullable=False)
    communes = db.relationship('Commune', backref='ile')
    Offres = db.relationship('Offres', backref='Ile')

    def __repr__(self):
        return f"('{self.ile_ID}', '{self.ile_Nom}', '{self.communes}'"