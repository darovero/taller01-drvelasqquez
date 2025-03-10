from .database import db

class Perro(db.Model):
    __tablename__ = 'perros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    peso = db.Column(db.Numeric(5,2))

    id_cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.id'))