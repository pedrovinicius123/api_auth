import requests
from requests.exceptions import JSONDecodeError, ConnectionError

base_url = "http://127.0.0.1:5000/hello"

# ==========================================
# FUNÇÃO AUXILIAR
# ==========================================

def exibir_resposta(response):

    print("Status:", response.status_code)

    print("\nCabeçalhos:")
    for chave, valor in response.headers.items():
        print(f"{chave}: {valor}")

    print("\nCorpo da resposta:")

    try:
        print(response.json())
    except JSONDecodeError:
        print(response.text)

# ==========================================
# 1. ACESSO SEM TOKEN
# ==========================================

print("=== TESTE 1 - SEM TOKEN ===")

try:

    response = requests.get(f"{base_url}/hello")

    exibir_resposta(response)

    if response.status_code == 401:
        print("\n✔ Status esperado")
    else:
        print("\n✘ Status inesperado")

except ConnectionError:
    print("✘ Não foi possível conectar na API")
    exit()

# ==========================================
# 2. LOGIN
# ==========================================

print("\n\n=== TESTE 2 - LOGIN JWT ===")

dados_login = {
    "username": "admin",
    "password": "123"
}

try:

    response = requests.post(
        f"{base_url}/login",
        json=dados_login
    )

    exibir_resposta(response)

    # Verifica sucesso
    if response.status_code != 200:
        print("\n✘ Login falhou")
        exit()

    # Tenta converter JSON
    try:
        dados = response.json()
    except JSONDecodeError:
        print("\n✘ Resposta não é JSON válido")
        exit()

    # Obtém token
    token = dados.get("access_token")

    if not token:
        print("\n✘ Token não encontrado")
        exit()

    print("\n✔ Token JWT recebido")

except ConnectionError:
    print("✘ Não foi possível conectar na API")
    exit()

# ==========================================
# 3. ACESSO COM TOKEN
# ==========================================

print("\n\n=== TESTE 3 - ACESSO COM JWT ===")

headers = {
    "Authorization": f"Bearer {token}"
}

try:

    response = requests.get(
        f"{base_url}/hello",
        headers=headers
    )

    exibir_resposta(response)

    if response.status_code == 200:
        print("\n✔ Recurso protegido acessado")
    else:
        print("\n✘ Falha ao acessar recurso protegido")

except ConnectionError:
    print("✘ Não foi possível conectar na API")