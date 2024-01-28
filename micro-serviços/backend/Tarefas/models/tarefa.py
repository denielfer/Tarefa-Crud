from ..db import Base
from sqlalchemy import Column as Col
import enum
from sqlalchemy import Integer, Date, Enum, VARCHAR,TEXT

class status_enum(enum.Enum):
    p='Pendente'
    e='Executando'
    c='Concluída'


class Tarefa(Base):
    __tablename__ = 'tarefa'
    id = Col(Integer(), primary_key=True)
    titulo = Col(VARCHAR(50), nullable=False)
    descricao = Col(TEXT)
    data = Col(Date, nullable=False)
    status = Col(Enum(status_enum), nullable=False)