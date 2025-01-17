""" The main file is where we initialize the flask application,
the database, marshamallow library and where we register our api blueprints."""
from flask import Flask 
from config import Config
from models.sqlalchemy.models import db, ma
from routes.sqlalchemy.candidates_response import response_routes
from routes.sqlalchemy.candidates import candidate_routes
from routes.sqlalchemy.question import question_routes
from routes.sqlalchemy.form import form_routes
from routes.sqlalchemy.location_resources import location_routes
from routes.sqlalchemy.location_response import location_response_routes
from routes.sqlalchemy.location_candidate import location_candidate_routes
# creates app


# Function that initializes the application. 
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    return app


app = create_app(Config)

# Connects the database to the application.
db.init_app(app)
with app.app_context():
    db.create_all()

# Bounds the scoped session created by SQLAlchemy to flask marshmallow schema.
ma.init_app(app)

# Blueprints for APIs
app.register_blueprint(candidate_routes, url_prefix='/api/v1/candidates')
app.register_blueprint(form_routes, url_prefix='/api/v1/forms')
app.register_blueprint(location_routes, url_prefix='/api/v1/locations')
app.register_blueprint(location_candidate_routes, url_prefix='/api/v1/locationcandidates')
app.register_blueprint(location_response_routes, url_prefix='/api/v1/locationresponses')
app.register_blueprint(question_routes, url_prefix='/api/v1/questions')
app.register_blueprint(response_routes, url_prefix='/api/v1/responses')
