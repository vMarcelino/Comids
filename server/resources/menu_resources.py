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


class MenuCreationEndpoint(flask_restful.Resource):
    def post(self):  # create

        # get fields info
        json = flask.request.json
        fields = ['name', 'place_id', 'token']
        helper_functions.check_missing_fields(json, *fields)
        name, place_id, token = map(lambda x: json[x], fields)

        # get user info (no need to check if the vertex is a User vertex as the token integrity is granted)
        administrator_id, _ = helper_functions.decode_jwt(jwt_token=token)
        admin_user_vertex = helper_functions.get_vertex_or_404(administrator_id, db.User)
        place_vertex = helper_functions.get_vertex_or_404(place_id, db.Place)

        #checks whether the user owns the place given
        place_count = admin_user_vertex.query().through_outgoing_edge(
            db.Administers).filter_by_property(id=place_vertex.graph_value.id).count().fetch_first()

        if place_count == 1:
            menu_query = place_vertex.query().through_edge(db.HasMenu)
            owned_menus_with_same_name_count = menu_query.filter_by_property(name=name).count().fetch_first()

            if owned_menus_with_same_name_count == 0:
                menu_vertex = db.Menu(name=name, place=place_vertex)
                menu_vertex.add_to_graph()
                return {"message": "Menu created", 'id': menu_vertex.graph_value.id}, HTTPStatus.OK

            else:
                return "There is already a manu with the same name", HTTPStatus.CONFLICT
        else:
            return "The user does not own the place", HTTPStatus.FORBIDDEN

    def put(self):  # update
        pass

    def delete(self):  # delete
        pass


class MenuListEndpoint(flask_restful.Resource):
    def get(self, menu_id=None, place_id=None):  # get
        if menu_id is not None:
            try:
                menu_vertex: db.Menu = janusgraphy.Query.from_vertex_id(menu_id).filter_by_property(
                    Label=db.Menu).fetch_first()
            except IndexError:
                return "Menu not found", HTTPStatus.NOT_FOUND

            menu_items = menu_vertex.query().through_outgoing_edge(db.HasItem).fetch_all()
            return {
                'properties': menu_vertex.Properties,
                'items': {item.graph_value.id: item.Properties
                          for item in menu_items}
            }, HTTPStatus.OK

        elif place_id is not None:
            try:
                place_vertex: db.Place = janusgraphy.Query.from_vertex_id(place_id).filter_by_property(
                    Label=db.Place).fetch_first()
            except IndexError:
                return "Place not found", HTTPStatus.NOT_FOUND

            menus = place_vertex.query().through_outgoing_edge(db.HasMenu).fetch_all()
            return {menu_vertex.graph_value.id: menu_vertex.Properties for menu_vertex in menus}, HTTPStatus.OK

