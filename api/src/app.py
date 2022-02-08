from flask import Flask
from flask_restx import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("src.config.Config")
CORS(app)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<User {self.name}>"


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}
