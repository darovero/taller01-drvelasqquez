from flask import Blueprint, render_template
from models.database import db
from models.perro import Perro
from models.cuidador import Cuidador

cuidadores_bp = Blueprint('cuidadores_bp', __name__, url_prefix='/cuidadores')

@cuidadores_bp.route('/mario')
def perros_de_mario():
    resultados = (
        db.session.query(Perro)
        .join(Cuidador)
        .filter(Cuidador.nombre == 'Mario')
        .all()
    )
    titulo = "Punto 2: Perros que cuida Mario"
    mensaje = f"Se encontraron {len(resultados)} perros que cuida Mario."
    return render_template('resultados.html', titulo=titulo, mensaje=mensaje, perros=resultados)
