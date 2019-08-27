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
    pass