from flask import Blueprint, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth_basic = HTTPBasicAuth()
bp_hello_basic = Blueprint("hello", __name__, url_prefix="/hello")

users = {
    "admin": generate_password_hash("123"),
}

@auth_basic.verify_password
def verify_password(username, password):
    """Callback function to validate credentials against database."""
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None



@bp_hello_basic.route("", methods=["GET"])
@auth_basic.login_required
def hello():
    user = auth_basic.current_user()
    return jsonify({
        "mensagem": f"Hello World! {user}"
    })
