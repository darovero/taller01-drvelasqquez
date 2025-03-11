from flask import Flask
from config import Config
from models.database import db
from flask_login import LoginManager
from controllers.auth_controller import auth
from controllers.main_views import main

app = Flask(__name__, template_folder="views")
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

from models.usuario import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

app.register_blueprint(auth)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)