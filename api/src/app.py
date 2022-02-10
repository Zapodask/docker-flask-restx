from flask import Flask
from flask_restx import Resource, Api
from flask_cors import CORS
from flask_migrate import Migrate

from .models import db
from .users.namespace import users


app = Flask(__name__)
app.config.from_object("src.config.Config")
CORS(app)
api = Api(app)

db.init_app(app)
migrate = Migrate(app, db)

api.add_namespace(users)
