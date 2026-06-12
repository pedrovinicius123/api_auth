import datetime
from flask import Blueprint, jsonify, request, g, current_app
from flask_httpauth import HTTPTokenAuth
import jwt

bp_route_jwt = Blueprint("jwt", __name__, url_prefix="/")

# Configura o HTTPAuth para ler o cabeçalho 'Authorization: Bearer <JWT>'
auth = HTTPTokenAuth(scheme='Bearer')

# Banco de dados simulado
USERS = {
    "admin":"123"
}

def generate_jwt(username):
    """Gera um token JWT válido por 30 minutos."""
    payload = {
        'sub': username,  # Subject (dono do token)
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)  # Expiração
    }
    return jwt.encode(payload, current_app.config.get("SECRET_KEY"))

@auth.verify_token
def verify_token(token):
    """Valida o token JWT extraído do cabeçalho."""
    try:
        # Decodifica e valida a assinatura/expiração do token
        payload = jwt.decode(token, current_app.config.get("SECRET_KEY"), algorithms=['HS256', "MD5"])
        g.current_user = payload['sub']
        return g.current_user
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido ou alterado

@bp_route_jwt.route('/login', methods=['POST'])
def login():
    """Rota pública para autenticar e obter o JWT."""
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    if username in USERS and USERS[username] == password:
        token = generate_jwt(username)
        return jsonify({'access_token': token})
    
    return jsonify({'error': 'Credenciais inválidas'}), 401

@bp_route_jwt.route('/hello', methods=['GET'])
@auth.login_required
def hello():
    """Rota privada que exige o JWT."""
    return jsonify({
        'message': f'Acesso autorizado para {g.current_user}!',
        'dados': 'Informações confidenciais aqui.'
    })
