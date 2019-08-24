import flask_restful
import flask
import jwt
import janusgraphy
from http import HTTPStatus

# import hack
import os, sys
print('===>', os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Local imports
import helper_functions  # pylint: disable=relative-beyond-top-level
from constants import CONSTANTS  # pylint: disable=relative-beyond-top-level
import db  # pylint: disable=relative-beyond-top-level


class PlaceEndpoint(flask_restful.Resource):
    def post(self):  # create
        json = flask.request.json

        are_fields_missing, missing_fields_message = helper_functions.are_fields_missing(json, 'name', 'token')
        if are_fields_missing:
            return missing_fields_message, HTTPStatus.BAD_REQUEST

        name = json['name']
        token = json['token']

        payload = jwt.decode(jwt=token, key=CONSTANTS.key, algorithms='HS256')
        administrator_id = payload['sub']

        admin_user_vertex = janusgraphy.Query.from_vertex_id(administrator_id).fetch_first()
        place_vertex = db.Place(name=name, adm=admin_user_vertex)
        place_vertex.add_to_graph()
        return {"message": "Place created", 'id': place_vertex.graph_value.id}, HTTPStatus.OK

    def put(self, administrator_id, place_id):  # update
        return "Not implemented yet", HTTPStatus.NOT_IMPLEMENTED

    def get(self, place_id):  # get
        return "Not implemented yet", HTTPStatus.NOT_IMPLEMENTED