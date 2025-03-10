from .database import db

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))

    perros = db.relationship('Perro', backref='cuidador', cascade='all, delete-orphan')
