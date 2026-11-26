import pytest
from tests.mocks.propostas import PROPOSTAS_MOCK


@pytest.mark.parametrize("proposta", PROPOSTAS_MOCK)
def test_cria_proposta(client, proposta, limpar_bd_teste):
    response = client.post( "/propostas", json=proposta)

    assert response.status_code == 201
    body = response.json()
    assert body["proposta"]["id"] == proposta['id']


def test_busca_lista_propostas(client, limpar_bd_teste):
    for proposta in PROPOSTAS_MOCK:
        client.post("/propostas", json=proposta)

    response = client.get(
        "/propostas",
    )

    body = response.json()
    assert response.status_code == 200
    assert len(body) == len(PROPOSTAS_MOCK)


@pytest.mark.parametrize("proposta", PROPOSTAS_MOCK)
def test_busca_proposta_por_id(client, proposta, limpar_bd_teste):
    client.post(
        "/propostas",
        json=proposta
    )
    response = client.get(
        f"/propostas/{proposta['id']}"
    )

    body = response.json()
    assert response.status_code == 200
    assert body["message"] == "Proposta encontrada"
    assert body["proposta"] == proposta