from flask import jsonify
from flask_restful import Resource
import datetime


class Natural_Timestamp(Resource):
    def get(self, endpoint_data):
        try:
            date = datetime.datetime.strptime(endpoint_data, '%B %d, %Y')
        except ValueError:
            return jsonify(unix=None,
                           natural=None)

        return jsonify(unix=int(date.timestamp()),
                       natural=date.strftime('%B %d, %Y'))


class Unix_Timestamp(Resource):
    def get(self, endpoint_data):
        date = datetime.datetime.utcfromtimestamp(endpoint_data)
        return jsonify(unix=int(date.timestamp()),
                       natural=date.strftime('%B %d, %Y'))
