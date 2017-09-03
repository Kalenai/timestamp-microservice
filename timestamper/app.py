from flask import Flask
from flask_restful import Api
from timestamper.resources.timestamp import Natural_Timestamp, Unix_Timestamp

app = Flask(__name__)
api = Api(app)


@app.route('/')
def homepage(self):
    return "Pass in a date as a Unix timestamp or a natural date timestamp of the form '<Month> <Day>, <Year>.'"


api.add_resource(Natural_Timestamp, '/<string:endpoint_data>')
api.add_resource(Unix_Timestamp, '/<int:endpoint_data>')
