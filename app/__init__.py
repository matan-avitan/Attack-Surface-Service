from flask import Flask
from flask_restful import Api
from app.resource import *


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Attack, "/api/v1/attack")
    api.add_resource(Statistic, "/api/v1/stats")

    return app
