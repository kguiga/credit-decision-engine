from fastapi import APIRouter, HTTPException, Depends
from app.schemas.proposta import RequestProposta
from app.services import proposta_service
from app.core.database import get_db

router = APIRouter()

@router.post("/propostas", status_code=201)
async def cria_proposta(proposta: RequestProposta, db=Depends(get_db)):
    try:
        proposta_service.criar_proposta(db, proposta)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return {
        "message": "Proposta criada com sucesso",
        "proposta": proposta
    } 


@router.get("/propostas")
async def get_propostas(db=Depends(get_db)):
    propostas = proposta_service.get_propostas(db)
    if propostas is None:
        return {
        "message": "Nenhuma proposta encontrada",
        "propostas": []
    }
    return propostas


@router.get("/propostas/{id}")
async def get_proposta(id: str, db=Depends(get_db)):
    proposta = proposta_service.get_proposta(db, id)
    if proposta is None:
        raise HTTPException(status_code=404, detail="Proposta não encontrada")
    return {
            "message": "Proposta encontrada", 
            "proposta": proposta
            }