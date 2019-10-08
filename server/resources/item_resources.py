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


class ItemCreationEndpoint(flask_restful.Resource):
    def post(self):  # create

        # get fields info
        json = flask.request.json
        fields = ['name', 'menu_id', 'value', 'description', 'token']
        helper_functions.check_missing_fields(json, *fields)
        name, menu_id, value, description, token = map(lambda x: json[x], fields)

        administrator_id, _ = helper_functions.decode_jwt(jwt_token=token)

        menu_vertex: db.Menu = janusgraphy.Query.from_vertex_id(menu_id).filter_by_property(Label=db.Menu).fetch_first()
        admin_id: db.User = janusgraphy.Query.from_vertex_id(administrator_id).filter_by_property(
            Label=db.User).fetch_first()

        count = admin_id.query().through_outgoing_edge(db.Administers).through_outgoing_edge(
            db.HasMenu).filter_by_property(id=menu_vertex.graph_value.id).count().fetch_first()

        if count == 1:
            menu_item_vertex = db.MenuItem(name=name, value=value, description=description, menu=menu_vertex)
            return {menu_item_vertex.graph_value.id: menu_item_vertex.Properties}, HTTPStatus.OK

        else:
            return 'No menu with id specified', HTTPStatus.NOT_FOUND

    def put(self):  # update
        pass

    def get(self):  # get
        pass

    def delete(self):  # delete
        pass
