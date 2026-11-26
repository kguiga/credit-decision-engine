import pytest
from sqlalchemy import text
from fastapi.testclient import TestClient
from main import app
from app.core.database import get_db
from app.core.database_test import get_test_db, SessionLocal
from tests.mocks.propostas import PROPOSTAS_MOCK


# preparação dos testes
@pytest.fixture
def client():
    app.dependency_overrides[get_db] = get_test_db # Permite substituir dependências do FastAPI durante os testes.

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()

@pytest.fixture
def limpar_bd_teste():
    session = SessionLocal()

    try:
        session.execute(text("TRUNCATE TABLE proposta;"))
        session.commit()
    
        yield

        session.execute(text("TRUNCATE TABLE proposta;"))
        session.commit()

    finally:
        session.close()
