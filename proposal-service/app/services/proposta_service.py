from app.repositories.proposta_repository import listar_propostas, buscar_proposta_por_id, salvar_proposta
from app.models.proposta import Proposta

def get_propostas(db):
    return listar_propostas(db)


def get_proposta(db, id: str):
    return buscar_proposta_por_id(id, db)


def criar_proposta(db, proposta):
    if buscar_proposta_por_id(proposta.id, db) is not None:
        raise ValueError("Proposta com o mesmo ID já existe.")
    proposta_model = Proposta(
        id=proposta.id,
        cpf=proposta.cpf,
        nome=proposta.nome,
        idade=proposta.idade,
        renda=proposta.renda,
        produto=proposta.produto,
    )

    return salvar_proposta(proposta_model, db)