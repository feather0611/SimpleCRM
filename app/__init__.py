from flask import Flask
from flask_restful_swagger_3 import Api, get_swagger_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import config as config

app = Flask(__name__)
CORS(app)
app.config.from_object(config.Config)
api = Api(app, version="1.0", title="Simple CRM API", description="Simple CRM API")
db = SQLAlchemy(app)

SWAGGER_URL = "/api/doc"
API_URL = "swagger.json"
swagger_blueprint = get_swagger_blueprint(
    api.open_api_object, swagger_prefix_url=SWAGGER_URL, swagger_url=API_URL
)

app.register_blueprint(swagger_blueprint)
