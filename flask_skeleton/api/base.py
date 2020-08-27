from flask_restful import Resource


class ApiBase(Resource):
    """docstring for ApiBase"""
    def get(self):
        return "/"
