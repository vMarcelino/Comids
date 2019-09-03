import flask_restful
import flask
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
        helper_functions.check_missing_fields(json, *fields)

        name, display_name, token = map(lambda x: json[x], fields)

        administrator_id, _ = helper_functions.decode_jwt(jwt_token=token)

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
        json = flask.request.args

        helper_functions.check_missing_fields(json, 'token')
        token = json['token']

        user_id, _ = helper_functions.decode_jwt(jwt_token=token)
        user_places = janusgraphy.Query.from_vertex_id(user_id).through_outgoing_edge(db.Administers).fetch_all()
        places_info = {p.graph_value.id: p.Properties for p in user_places}

        if place_id in places_info:
            return places_info[place_id], HTTPStatus.OK
        else:
            return 'Place not found or not authorized', HTTPStatus.NOT_FOUND


class ListPlacesEndpoint(flask_restful.Resource):
    def get(self):
        places = db.Place.query().fetch_all()
        places_info = {p.graph_value.id: p.Properties for p in places}
        return places_info