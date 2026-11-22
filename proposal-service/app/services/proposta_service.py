propostas = []

def get_propostas():
    return propostas if len(propostas) > 0 else None


def get_proposta(id: int):
    for pro in propostas:
        if pro["id"] == id:
            return pro
    return None