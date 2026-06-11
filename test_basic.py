import requests

url = "http://127.0.0.1:5000/hello"

# ==========================================
# 1. REQUISIÇÃO SEM AUTENTICAÇÃO
# ==========================================

print("=== TESTE 1 - SEM AUTENTICAÇÃO ===")

response = requests.get(url)

print("Status recebido:", response.status_code)

# Verifica se retornou 401
if response.status_code == 401:
    print("✔ Status 401 Unauthorized recebido corretamente")
else:
    print("✘ ERRO: status inesperado")

# Verifica cabeçalho WWW-Authenticate
www_auth = response.headers.get("WWW-Authenticate", "")

if www_auth:
    print("✔ Cabeçalho WWW-Authenticate encontrado")
    print("Valor:", www_auth)
else:
    print("✘ ERRO: cabeçalho WWW-Authenticate ausente")

# Verifica estratégia Basic
if "Basic" in www_auth:
    print("✔ Estratégia Basic identificada")
else:
    print("✘ ERRO: estratégia Basic não encontrada")

# Verifica o realm
if 'realm="Authentication Required"' in www_auth:
    print("✔ Realm padrão identificado")
else:
    print("✘ ERRO: realm inesperado")

# Verifica se a rota acessada é /hello
if response.request.path_url == "/hello":
    print("✔ Recurso /hello acessado corretamente")
else:
    print("✘ ERRO: rota incorreta")

print("\nResposta do servidor:")
print(response.text)

# ==========================================
# 2. REQUISIÇÃO COM BASIC AUTH
# ==========================================

print("\n\n=== TESTE 2 - COM BASIC AUTH ===")

response = requests.get(
    url,
    auth=("admin", "123")
)

print("Status recebido:", response.status_code)

# Verifica se retornou 200
if response.status_code == 200:
    print("✔ Status 200 OK recebido corretamente")
else:
    print("✘ ERRO: status inesperado")

# Verifica se a rota acessada é /hello
if response.request.path_url == "/hello":
    print("✔ Recurso /hello acessado corretamente")
else:
    print("✘ ERRO: rota incorreta")

# Verifica se enviou cabeçalho Authorization
authorization = response.request.headers.get("Authorization")

if authorization:
    print("✔ Cabeçalho Authorization enviado")
    print("Valor:", authorization)
else:
    print("✘ ERRO: Authorization não enviado")

# Verifica se o tipo de autenticação é Basic
if authorization.startswith("Basic "):
    print("✔ Cabeçalho Basic enviado corretamente")
else:
    print("✘ ERRO: cabeçalho não utiliza Basic")

print("\nResposta do servidor:")
print(response.text)