from app.core.database import SessionLocal
from app.models.proposta import Proposta

def listar_propostas():
    session = SessionLocal()
    try:
        return session.query(Proposta).all()
    finally:
        session.close()


def buscar_proposta_por_id(id):
    session = SessionLocal()
    try:
        return session.query(Proposta).where(Proposta.id == id).first()
    finally:
        session.close()


def salvar_proposta(proposta):
    session = SessionLocal()
    try:
        session.add(proposta)
        session.commit()
        return proposta
        
    finally:
        session.close()