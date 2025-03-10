from flask import Blueprint, render_template
from models.perro import Perro

perros_bp = Blueprint('perros_bp', __name__, url_prefix='/perros')

@perros_bp.route('/lassie')
def perros_lassie():
    lista_lassie = Perro.query.filter_by(nombre='Lassie').all()
    titulo = "Punto 1: Perros llamados Lassie"
    mensaje = f"Se encontraron {len(lista_lassie)} perros llamados Lassie."
    return render_template('resultados.html', titulo=titulo, mensaje=mensaje, perros=lista_lassie)
