from fastapi import APIRouter, HTTPException
from app.schemas.proposta import RequestProposta
from app.services import proposta_service

router = APIRouter()

@router.post("/propostas", status_code=201)
async def cria_proposta(proposta: RequestProposta):
    return {
        "message": "Proposta criada com sucesso",
        "proposta": proposta
    }


@router.get("/propostas")
async def get_propostas():
    propostas = proposta_service.get_propostas()
    if propostas is None:
        return {
        "message": "Nenhuma proposta encontrada",
        "propostas": []
    }
    return propostas



@router.get("/propostas/{id}")
async def get_proposta(id: int):
    proposta = proposta_service.get_proposta(id)
    if proposta is None:
        raise HTTPException(status_code=404, detail="Proposta não encontrada")
    return {
            "message": "Proposta encontrada", 
            "proposta": proposta
            }