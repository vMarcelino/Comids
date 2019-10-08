import flask
import flask_restful
from flask_cors import CORS

# Local imports
import db
import resources

app = flask.Flask(__name__)
CORS(app)
api = flask_restful.Api(app)

db.connect()

api.add_resource(resources.UserCreationEndpoint, '/signup')  # creates user and returns token
api.add_resource(resources.UserAuthenticationEndpoint, '/auth')  # gets token for existing user
api.add_resource(resources.UserPlaceInfoEndpoint, '/myPlaces')  # list user places
api.add_resource(resources.PlaceEndpoint, '/place')  # create, get, update, delete a place
api.add_resource(resources.ListPlacesEndpoint, '/place/list')  # list all places
api.add_resource(resources.MenuListEndpoint, '/place/menu/list/<int:place_id>', '/menu/<int:menu_id>')
api.add_resource(resources.MenuCreationEndpoint, '/menu')  # create, get, update, delete a menu
api.add_resource(resources.ItemCreationEndpoint, '/menu/item/create')
api.add_resource(resources.UserOrderEndpoint, '/order')
api.add_resource(resources.UserOrderAcceptEndpoint, '/order/accept')


#@api.representation('application/json')
#def output_json(data, code, headers
def run():
    app.run(host='0.0.0.0', port=2283)


if __name__ == "__main__":
    run()