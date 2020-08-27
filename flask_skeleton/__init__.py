from flask import Flask
from .database import init_db

__version__ = "0.0.0"


def load_blueprints(app):
    if app.config["REGISTER_CORE"]:
        from flask_skeleton.core import routes

        app.register_blueprint(routes.blueprint)


def create_app(config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    init_db(app)
    
    load_blueprints(app)

    return app
