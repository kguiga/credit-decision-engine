from app.repositories.proposta_repository import listar_propostas, buscar_proposta_por_id, salvar_proposta

def get_propostas():
    return listar_propostas()


def get_proposta(id: int):
    return buscar_proposta_por_id(id)


def criar_proposta(proposta: dict):
    if buscar_proposta_por_id(proposta["id"]) is not None:
        raise ValueError("Proposta com o mesmo ID já existe.")
    return salvar_proposta(proposta)