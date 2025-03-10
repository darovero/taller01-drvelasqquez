from flask import Flask
from config import Config
from models.database import db
from controllers.main_views import main_bp
from controllers.perros_controller import perros_bp
from controllers.cuidadores_controller import cuidadores_bp

def create_app():
    app = Flask(__name__, template_folder="views")
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(main_bp)
    app.register_blueprint(perros_bp)
    app.register_blueprint(cuidadores_bp)

    return app

if __name__ == '__main__':
    app_instance = create_app()
    with app_instance.app_context():
        db.create_all()
    app_instance.run(debug=True)
