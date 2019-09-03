import flask
import flask_restful

# Local imports
import db
import resources

app = flask.Flask(__name__)
api = flask_restful.Api(app)

db.connect()

api.add_resource(resources.UserCreationEndpoint, '/signup')
api.add_resource(resources.UserAuthenticationEndpoint, '/auth')
api.add_resource(resources.UserPlaceInfoEndpoint, '/places/info')
api.add_resource(resources.PlaceEndpoint, '/place')
api.add_resource(resources.ListPlacesEndpoint, '/place/list')


def run():
    app.run(host='0.0.0.0', port=2283)


if __name__ == "__main__":
    run()