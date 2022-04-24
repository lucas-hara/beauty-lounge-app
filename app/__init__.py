from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Inicializa o banco de dados
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "t45_d%>gy+a]zE`w:&6oqRU<?sgKbC"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # Registro das blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app