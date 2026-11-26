from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

PROPOSTA_VALIDA = {
                "id": "PROP-999",
                "cpf": "12345678901",
                "nome": "Cliente Teste 1",
                "idade": 25,
                "renda": 3000,
                "produto": "CARTAO"
            }

def test_cria_proposta():
    TRUNCATE TABLE proposta;
    response = client.post(
        "/propostas",
        json=PROPOSTA_VALIDA
    )

    assert response.status_code == 201


def test_busca_lista_propostas():
    response = client.get(
        "/propostas",
    )

    assert response.status_code == 200


def test_busca_proposta_por_id():
    client.post(
        "/propostas",
        json=PROPOSTA_VALIDA
    )
    response = client.get(
        f"/propostas/{PROPOSTA_VALIDA['id']}"
    )

    assert response.status_code == 200
    assert response.json() == PROPOSTA_VALIDA