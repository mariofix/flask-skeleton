from peewee import *
from playhouse.flask_utils import FlaskDB


def init_db(app):
    db = FlaskDB()
    db.init_app(app)
