from pydantic import BaseModel, Field

class RequestProposta(BaseModel):
   
    id: str = Field(..., description="ID da proposta", max_length=36)
    cpf: str = Field(..., description="CPF do solicitante", max_length=11, min_length=11)
    nome: str = Field(..., description="Nome do solicitante", max_length=100)
    idade: int = Field(..., description="Idade do solicitante", ge=0)
    renda: float = Field(..., description="Renda do solicitante", gt=0)
    produto: str = Field(..., description="Produto solicitado", max_length=50)