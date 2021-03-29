from flask import Flask
from flask_restful import Api
from app.resource import *
from app.models import db
from app.utils import setup_data_to_db


def create_app(inputs):
    app = Flask(__name__)
    api = Api(app)

    # config and init the db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    # add routes
    api.add_resource(Attack, "/api/v1/attack")
    api.add_resource(Statistic, "/api/v1/stats")

    # drop old table and create new from modals
    with app.app_context():
        db.drop_all()
        db.create_all()
        setup_data_to_db(inputs)

    return app
