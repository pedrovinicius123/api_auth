import requests

url = "http://127.0.0.1:5000/hello"

# ==========================================
# 1. REQUISIÇÃO SEM API KEY
# ==========================================

print("=== TESTE 1 - SEM API KEY ===")

response = requests.get(url)

print("Status recebido:", response.status_code)

# Verifica status 401
if response.status_code == 401:
    print("✔ Status 401 Unauthorized recebido corretamente")
else:
    print("✘ ERRO: status inesperado")

# Verifica rota
if response.request.path_url == "/hello":
    print("✔ Recurso /hello acessado corretamente")
else:
    print("✘ ERRO: rota incorreta")

# Verifica ausência do cabeçalho
if "x-api-key" not in response.request.headers:
    print("✔ Cabeçalho x-api-key ausente conforme esperado")
else:
    print("✘ ERRO: cabeçalho inesperado")

print("\nResposta:")
print(response.text)

# ==========================================
# 2. REQUISIÇÃO COM API KEY INVÁLIDA
# ==========================================

print("\n\n=== TESTE 2 - API KEY INVÁLIDA ===")

headers = {
    "x-api-key": "CHAVE_ERRADA"
}

response = requests.get(
    url,
    headers=headers
)

print("Status recebido:", response.status_code)

# Verifica status 403
if response.status_code == 403:
    print("✔ Status 403 Forbidden recebido corretamente")
else:
    print("✘ ERRO: status inesperado")

# Verifica envio do cabeçalho
if response.request.headers.get("x-api-key"):
    print("✔ Cabeçalho x-api-key enviado")
else:
    print("✘ ERRO: cabeçalho não enviado")

# Verifica rota
if response.request.path_url == "/hello":
    print("✔ Recurso /hello acessado corretamente")
else:
    print("✘ ERRO: rota incorreta")

print("\nResposta:")
print(response.text)

# ==========================================
# 3. REQUISIÇÃO COM API KEY VÁLIDA
# ==========================================

print("\n\n=== TESTE 3 - API KEY VÁLIDA ===")

headers = {
    "x-api-key": "MINHA_CHAVE_SECRETA"
}

response = requests.get(
    url,
    headers=headers
)

print("Status recebido:", response.status_code)

# Verifica status 200
if response.status_code == 200:
    print("✔ Status 200 OK recebido corretamente")
else:
    print("✘ ERRO: status inesperado")

# Verifica envio do cabeçalho
if response.request.headers.get("x-api-key"):
    print("✔ Cabeçalho x-api-key enviado")
    print("Valor:", response.request.headers.get("x-api-key"))
else:
    print("✘ ERRO: cabeçalho não enviado")

# Verifica rota
if response.request.path_url == "/hello":
    print("✔ Recurso /hello acessado corretamente")
else:
    print("✘ ERRO: rota incorreta")

print("\nResposta:")
print(response.text)