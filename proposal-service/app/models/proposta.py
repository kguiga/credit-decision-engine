from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Numeric
from decimal import Decimal 

# Representar a tabela proposta como uma classe
class Proposta(Base):
    __tablename__ = "proposta"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    renda: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    produto: Mapped[str] = mapped_column(String(50), nullable=False)