import flask_restful
import flask
import janusgraphy
from http import HTTPStatus
from typing import List

# import hack
import os, sys
print('===>', os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Local imports
import helper_functions  # pylint: disable=relative-beyond-top-level
from constants import CONSTANTS  # pylint: disable=relative-beyond-top-level
import db  # pylint: disable=relative-beyond-top-level


class UserCreationEndpoint(flask_restful.Resource):
    def post(self):
        json = flask.request.json

        helper_functions.check_missing_fields(json, 'user', 'password')

        username = json['user']
        password = json['password']

        if len(list(db.User.query().filter_by_property(name=username).fetch_all())) == 0:
            if len(password) >= CONSTANTS.min_password_len:
                salt = helper_functions.generate_cryptographically_random_string(8)
                hashed_password = helper_functions.hash_with_salt(password, salt)
                user_vertex = db.User(name=username, password=hashed_password, salt=salt)
                user_vertex.add_to_graph()
                encoded = helper_functions.generate_jwt(user_vertex)
                return {'token': encoded}, HTTPStatus.CREATED

            else:
                return f'Password too short. Minimum {CONSTANTS.min_password_len} characters long', HTTPStatus.NOT_ACCEPTABLE

        else:
            return 'Username already in use', HTTPStatus.CONFLICT


class UserAuthenticationEndpoint(flask_restful.Resource):
    def post(self):
        json = flask.request.json

        helper_functions.check_missing_fields(json, 'user', 'password')

        username = json['user']
        password = json['password']

        try:
            user_vertex = db.User.query().filter_by_property(name=username).fetch_first()
        except:
            # wrong username
            return "Wrong username or password", HTTPStatus.UNAUTHORIZED

        saved_password = user_vertex.Properties['password']
        used_salt = user_vertex.Properties['salt']

        computed_password = helper_functions.hash_with_salt(password, used_salt)

        if computed_password == saved_password:
            encoded = helper_functions.generate_jwt(user_vertex)
            return {'token': encoded}, HTTPStatus.ACCEPTED

        else:
            # wrong password
            return "Wrong username or password", HTTPStatus.UNAUTHORIZED


class UserPlaceInfoEndpoint(flask_restful.Resource):
    def get(self):
        json = flask.request.args

        helper_functions.check_missing_fields(json, 'token')
        token = json['token']

        user_id, _ = helper_functions.decode_jwt(jwt_token=token)
        user_places = janusgraphy.Query.from_vertex_id(user_id).through_outgoing_edge(db.Administers).fetch_all()

        return {p.graph_value.id: p.Properties for p in user_places}, HTTPStatus.OK


class UserOrderEndpoint(flask_restful.Resource):
    def get(self):
        json = flask.request.args

        fields = ['place_id', 'token']
        helper_functions.check_missing_fields(json, *fields)
        place_id, token = map(lambda x: json[x], fields)

        place_vertex: db.Place = helper_functions.get_vertex_or_404(place_id, db.Place)
        user_id, _ = helper_functions.decode_jwt(jwt_token=token)

        q_relation = janusgraphy.Query.relation()  # represents the order
        q_relation.through_incoming_edge(db.Orders).filter_by_property(id=user_id, Label=db.User)

        user_orders_from_place_q = place_vertex.query()
        user_orders_from_place_q.filter_by_incoming_edge(db.From)
        user_orders_from_place_q.filter_by_relation(q_relation)
        user_orders_from_place: List[db.Order] = user_orders_from_place_q.fetch_all()
        orders = {}
        for order in user_orders_from_place:
            q = order.query()
            q.through_outgoing_edge(db.Has)
            q.filter_by_property(Label=db.MenuItem)
            items: List[db.MenuItem] = q.fetch_all()
            orders[order.graph_value.id] = [{item.graph_value.id: item.Properties} for item in items]

        return orders, HTTPStatus.OK

    def post(self):  # create order (at least one item needed)
        # get fields info
        json = flask.request.json
        fields = ['place_id', 'item_id', 'token']
        helper_functions.check_missing_fields(json, *fields)
        place_id, item_id, token = map(lambda x: json[x], fields)

        user_id, _ = helper_functions.decode_jwt(jwt_token=token)

        place_vertex: db.Place = helper_functions.get_vertex_or_404(place_id, db.Place)
        user_vertex: db.User = helper_functions.get_vertex_or_404(user_id, Label=db.User)
        item_vertex: db.MenuItem = helper_functions.get_vertex_or_404(item_id, Label=db.MenuItem)

        is_item_from_place = item_vertex.query().through_incoming_edge(db.HasItem).through_incoming_edge(
            db.HasMenu).filter_by_property(id=place_id).count().fetch_first() == 1

        if is_item_from_place:
            order_vertex = db.Order(False, place_vertex, user_vertex)
            order_vertex.add_item(item_vertex)

        else:
            return 'Item is not from the specified place', HTTPStatus.NOT_FOUND

    def put(self):  # add item to order
        # get fields info
        json = flask.request.json
        fields = ['order_id', 'item_id', 'token']
        helper_functions.check_missing_fields(json, *fields)
        order_id, item_id, token = map(lambda x: json[x], fields)

        user_id, _ = helper_functions.decode_jwt(jwt_token=token)

        order_vertex: db.Order = helper_functions.get_vertex_or_404(order_id, db.Place)
        item_vertex: db.MenuItem = helper_functions.get_vertex_or_404(item_id, Label=db.MenuItem)

        if order_vertex.is_from_user(user_id):
            order_vertex.add_item(item_vertex)

        else:
            return 'Invalid order id', HTTPStatus.NOT_FOUND


class UserOrderAcceptEndpoint(flask_restful.Resource):
    def put(self):
        json = flask.request.json
        fields = ['order_id', 'token']
        helper_functions.check_missing_fields(json, *fields)
        order_id, token = map(lambda x: json[x], fields)

        user_id, _ = helper_functions.decode_jwt(jwt_token=token)

        order_vertex = helper_functions.get_vertex_or_404(order_id, db.Order)
        if order_vertex.is_from_user(user_id):
            order_vertex.accept()
        else:
            return 'Invalid order id', HTTPStatus.NOT_FOUND
