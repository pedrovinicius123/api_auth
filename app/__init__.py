from flask import Flask
from app.routes.hello_route_basic import bp_hello_basic
from app.routes.hello_route_digest import bp_hello_digest
from dotenv import load_dotenv
import os
load_dotenv()

def create_app():
    # App
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Register blueprints
    #app.register_blueprint(bp_hello_basic)
    app.register_blueprint(bp_hello_digest)

    return app
