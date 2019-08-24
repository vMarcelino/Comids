import flask_restful
import flask
import jwt
import datetime
from http import HTTPStatus

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

        are_fields_missing, missing_fields_message = helper_functions.are_fields_missing(json, 'user', 'password')
        if are_fields_missing:
            return missing_fields_message, HTTPStatus.BAD_REQUEST

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

        are_fields_missing, missing_fields_message = helper_functions.are_fields_missing(json, 'user', 'password')
        if are_fields_missing:
            return missing_fields_message, HTTPStatus.BAD_REQUEST

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
