from app.repositories.proposta_repository import listar_propostas, buscar_proposta_por_id, salvar_proposta
from app.models.proposta import Proposta

def get_propostas():
    return listar_propostas()


def get_proposta(id: int):
    return buscar_proposta_por_id(id)


def criar_proposta(proposta=dict):
    if buscar_proposta_por_id(proposta.id) is not None:
        raise ValueError("Proposta com o mesmo ID já existe.")
    proposta_model = Proposta(
        id=proposta.id,
        cpf=proposta.cpf,
        nome=proposta.nome,
        idade=proposta.idade,
        renda=proposta.renda,
        produto=proposta.produto,
    )

    return salvar_proposta(proposta_model)