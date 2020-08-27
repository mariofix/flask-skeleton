from flask import Flask
from flask_restful import Api
from flask_skeleton.api.base import ApiBase
__version__ = "0.0.0"


def load_api(app):
    api = Api(app)
    api.add_resource(ApiBase, "/")


def create_app(config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    load_api(app)

    return app
