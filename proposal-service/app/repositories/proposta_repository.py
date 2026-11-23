propostas = []

def listar_propostas():
    return propostas if len(propostas) > 0 else None


def buscar_proposta_por_id(id):
    for pro in propostas:
        if pro["id"] == id:
            return pro
    return None


def salvar_proposta(proposta):
    propostas.append(proposta)
    return proposta