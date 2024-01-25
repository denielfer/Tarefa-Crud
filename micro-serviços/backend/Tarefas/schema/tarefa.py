from pydantic import BaseModel
from datetime import date
from typing import List

class complet_tarefa_schema(BaseModel):
    id:int
    titulo:str
    descricao:str
    data:date
    status:str

class list_tarefas_schema(BaseModel):
    tarefas:List[complet_tarefa_schema]

class put_post_tarefa_schema(BaseModel):
    titulo:str
    descricao:str
    data:date
    status:str

class compact_tarefa_schema(BaseModel):
    id:int
    titulo:str
    data:date
    status:str
    
class slice_tarefas_schema(BaseModel):
    tarefas:List[compact_tarefa_schema]