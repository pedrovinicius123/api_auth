import requests
from requests.auth import HTTPDigestAuth

url = "http://127.0.0.1:5000/hello"

# ==========================================
# 1. REQUISIÇÃO SEM AUTENTICAÇÃO
# ==========================================

print("=== TESTE 1 - SEM AUTENTICAÇÃO ===")

response = requests.get(url)

print("Status recebido:", response.status_code)

# Verifica status 401
if response.status_code == 401:
    print("✔ Status 401 Unauthorized recebido corretamente")
else:
    print("✘ ERRO: status inesperado")

# Verifica cabeçalho WWW-Authenticate
www_auth = response.headers.get("WWW-Authenticate")

if www_auth:
    print("✔ Cabeçalho WWW-Authenticate encontrado")
    print("Valor:")
    print(www_auth)
else:
    print("✘ ERRO: cabeçalho ausente")

# Verifica Digest
if "Digest" in www_auth:
    print("✔ Estratégia Digest identificada")
else:
    print("✘ ERRO: estratégia Digest não encontrada")

# Verifica realm
if 'realm="hello"' in www_auth:
    print("✔ Realm identificado")
else:
    print("✘ ERRO: realm inesperado")

# Verifica nonce
if "nonce=" in www_auth:
    print("✔ Nonce enviado pelo servidor")
else:
    print("✘ ERRO: nonce ausente")

# Verifica qop
if "qop=" in www_auth:
    print("✔ qop enviado")
else:
    print("✘ ERRO: qop ausente")

# Verifica rota
if response.request.path_url == "/hello":
    print("✔ Recurso /hello acessado corretamente")
else:
    print("✘ ERRO: rota incorreta")

print("\nResposta:")
print(response.text)

# ==========================================
# 2. REQUISIÇÃO COM DIGEST AUTH
# ==========================================

print("\n\n=== TESTE 2 - COM DIGEST AUTH ===")

response = requests.get(
    url,
    auth=HTTPDigestAuth("admin", "123")
)

print("Status recebido:", response.status_code)

# Verifica status 200
if response.status_code == 200:
    print("✔ Status 200 OK recebido corretamente")
else:
    print("✘ ERRO: status inesperado")

# Verifica rota
if response.request.path_url == "/hello":
    print("✔ Recurso /hello acessado corretamente")
else:
    print("✘ ERRO: rota incorreta")

# Verifica cabeçalho Authorization
authorization = response.request.headers.get("Authorization")

if authorization:
    print("✔ Cabeçalho Authorization enviado")
else:
    print("✘ ERRO: Authorization ausente")

print("\nCabeçalho Authorization enviado:")
print(authorization)

print("\nResposta:")
print(response.text)