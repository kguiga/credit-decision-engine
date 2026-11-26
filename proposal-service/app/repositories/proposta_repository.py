from app.core.database import SessionLocal
from app.models.proposta import Proposta

def listar_propostas(session):
    return session.query(Proposta).all()


def buscar_proposta_por_id(id, session):
    return session.query(Proposta).where(Proposta.id == id).first()


def salvar_proposta(proposta, session):
    session.add(proposta)
    session.commit()