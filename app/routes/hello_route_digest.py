from flask import Blueprint, jsonify
from flask_httpauth import HTTPDigestAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth_digest = HTTPDigestAuth(realm="hello")
bp_hello_digest = Blueprint("hello", __name__, url_prefix="/hello")

users = {
    "admin": "123",
}

@auth_digest.get_password
def get_pw(username):
    """Callback function that returns the password for a given user."""
    if username in users:
        return users.get(username)
    return None



@bp_hello_digest.route("", methods=["GET"])
@auth_digest.login_required
def hello():
    user = auth_digest.current_user()
    return jsonify({
        "mensagem": f"Hello World! {user}"
    })