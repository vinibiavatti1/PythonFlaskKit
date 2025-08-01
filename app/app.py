from flask import Flask
from app.blueprints import blueprints
from dotenv import load_dotenv
import os


def create_app(name: str, env_path: str) -> Flask:
    load_dotenv(env_path)
    app = Flask(name)
    app.env = os.getenv('ENV')
    app.secret_key = os.getenv('SECRET_KEY')
    [app.register_blueprint(x) for x in blueprints]
    return app
