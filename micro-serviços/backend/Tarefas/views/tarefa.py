from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import Tarefas.schema.tarefa as Schema
from Tarefas.models.tarefa import Tarefa
from Tarefas.db import SessionLocal
from sqlalchemy import exc

router = APIRouter()

# remover descrição da lista de tarefas?
@router.get(
    path='/tarefa/',
    response_model=Schema.list_tarefas_schema,
)
async def all_tarefas():
    session = SessionLocal()
    response = {'tarefas':[]}
    try:
        tarefas = session.query(Tarefa).all()
        response['tarefas'] = [ 
                    {
                        "id":tarefa.id,
                        "titulo":tarefa.titulo,
                        'descricao':tarefa.descricao,
                        'data':tarefa.data,
                        'status':tarefa.status,
                    } for tarefa in tarefas
                  ]
    except Exception as e:
            response = {"error": "internal", 'msg':str(e)}
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content=response, status_code=status_code)
    finally:
        session.close()
    return response

@router.get(
    path='/tarefa/{id}',
    response_model=Schema.complet_tarefa_schema
)
async def get_tarefa(id:int):
    session = SessionLocal()
    tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
    try:
        if not tarefa:
            response = {"error": "Tarefa especificada não foi encontrada!"}
            status_code = status.HTTP_404_NOT_FOUND
            return JSONResponse(content=response, status_code=status_code)
        response:Schema.complet_tarefa_schema = { 
            'id':tarefa.id,
            'titulo':tarefa.titulo,
            'descricao':tarefa.descricao,
            'data':tarefa.data,
            'status':tarefa.status
         }
    finally:
        session.close()
    return response

@router.delete(
    path='/tarefa/{id}',
    response_model=Schema.complet_tarefa_schema
)
async def delete_tarefa(id:int):
    session = SessionLocal()
    tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
    try:
        if not tarefa:
            response = {"error": "Tarefa especificada não foi encontrada!"}
            status_code = status.HTTP_404_NOT_FOUND
            return JSONResponse(content=response, status_code=status_code)
        response:Schema.complet_tarefa_schema = { 
            'id':tarefa.id,
            'titulo':tarefa.titulo,
            'descricao':tarefa.descricao,
            'data':tarefa.data,
            'status':tarefa.status
         }
        session.delete(tarefa)
        session.flush()
        session.commit()
    finally:
        session.close()
    return response

@router.post(
    path='/tarefa/',
)
async def create_tarefa(rbody: Schema.put_post_tarefa_schema):
    session = SessionLocal()
    try:
        print(rbody,type(rbody))
        tarefa = Tarefa(**dict(rbody))
        session.add(tarefa)
        session.flush()
        session.commit()
    except exc.SQLAlchemyError as e:
        print(e)
        status_code = status.HTTP_400_BAD_REQUEST
        response = {"error": "Problema nos dados fornecidos", "msg":str(e)}
        return JSONResponse(content=response, status_code=status_code)
    except Exception as ex:
        response = {"error": str(ex)}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=response, status_code=status_code)
    finally:
        session.close()
    return {"msg":"Tarefa criada com sucesso"}

# fazer UPDATE
@router.put(
    path='/tarefa/{id}',
)
async def edit_tarefa(id:int,rbody: Schema.put_post_tarefa_schema):
    session = SessionLocal()
    tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
    if not tarefa:
        response = {"error": "Tarefa não encontrada"}
        status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(content=response, status_code=status_code)
    try:
        tarefa.titulo = rbody.titulo
        tarefa.descricao = rbody.descricao
        tarefa.data = rbody.data
        tarefa.status = rbody.status
        session.add(tarefa)
        session.flush()
        session.commit()
    except exc.SQLAlchemyError as e:
        status_code = status.HTTP_400_BAD_REQUEST
        response = {"error": "Problema nos dados fornecidos", "msg":str(e)}
        return JSONResponse(content=response, status_code=status_code)
    except Exception as ex:
        response = {"error": str(ex)}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=response, status_code=status_code)
    finally:
        session.close()
    return {"msg":"Tarefa criada com sucesso"}