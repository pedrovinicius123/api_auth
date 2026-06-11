from flask import Blueprint, jsonify
from flask_httpauth import HTTPTokenAuth

auth_token = HTTPTokenAuth(sheme="Bearer ")
bp_hello_token = Blueprint("hello", __name__, url_prefix="/hello")

api_keys = {
    "x_api_key":"admin",
}

@auth_token.verify_token
def verify_token(token):
    # Check if the provided API key exists in your system
    if token in api_keys:
        return "admin" == api_keys[token] # Returns the user identity
    return None


@bp_hello_token.route("", methods=["GET"])
@auth_token.login_required
def hello():
    user = auth_token.current_user()
    return jsonify({
        "mensagem": f"Hello World! {user}"
    })
