from flask import Flask
from flask_restful import Api
from app.resources.timestamp import Natural_Timestamp, Unix_Timestamp
from app.config import *

app = Flask(__name__)
api = Api(app)

app.config.from_object(DevelopmentConfig)

api.add_resource(Natural_Timestamp, '/<string:endpoint_data>')
api.add_resource(Unix_Timestamp, '/<int:endpoint_data>')

from app import views
