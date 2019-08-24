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
        fields = ['name', 'display_name', 'token']
        are_fields_missing, missing_fields_message = helper_functions.are_fields_missing(json, *fields)
        if are_fields_missing:
            return missing_fields_message, HTTPStatus.BAD_REQUEST

        name = json['name']
        display_name = json['display_name']
        token = json['token']

        payload = jwt.decode(jwt=token, key=CONSTANTS.key, algorithms='HS256')
        administrator_id = payload['sub']

        admin_user_vertex = janusgraphy.Query.from_vertex_id(administrator_id).fetch_first()

        owned_places_query = admin_user_vertex.query().through_outgoing_edge(db.Administers)
        owned_places_with_same_name = list(owned_places_query.filter_by_property(name=name).fetch_all())

        if len(owned_places_with_same_name) == 0:
            place_vertex = db.Place(name=name, display_name=display_name, adm=admin_user_vertex)
            place_vertex.add_to_graph()
            return {"message": "Place created", 'id': place_vertex.graph_value.id}, HTTPStatus.OK

        else:
            return "There is already a place with the same name", HTTPStatus.CONFLICT

    def put(self, administrator_id, place_id):  # update
        return "Not implemented yet", HTTPStatus.NOT_IMPLEMENTED

    def get(self, place_id):  # get
        return "Not implemented yet", HTTPStatus.NOT_IMPLEMENTED