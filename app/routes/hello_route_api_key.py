from flask import Blueprint, jsonify
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import Forbidden

auth_token = HTTPTokenAuth(header="x-api-key")
bp_hello_token = Blueprint("hello", __name__, url_prefix="/hello")

api_keys = {
    "MINHA_CHAVE_SECRETA":"admin",
}

@auth_token.verify_token
def verify_token(token):
    # Check if the provided API key exists in your system
    if not token:
        return None
    if token in api_keys:
        return api_keys[token] # Returns the user identity
    raise Forbidden()  

@bp_hello_token.errorhandler(Forbidden)
def handle_forbidden(e):
    return jsonify({
        "erro": "Acesso proibido",
        "mensagem": str(e.description)
    }), 403


@bp_hello_token.route("", methods=["GET"])
@auth_token.login_required
def hello():
    user = auth_token.current_user()
    print(user)
    return jsonify({
        "mensagem": f"Hello World! {user}"
    })
