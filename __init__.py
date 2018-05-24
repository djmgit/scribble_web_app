import os
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'secret'
    app.config['admin_token'] = "Bearer 1f3e1016c00260a82f3f38c820d012330ea673c0d04a6153"
    CORS(app, resources={r"*": {"origins": "*"}})

    return app
