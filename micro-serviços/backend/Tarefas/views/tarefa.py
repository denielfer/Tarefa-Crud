from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
import Tarefas.schema.tarefa as Schema
from Tarefas.models.tarefa import Tarefa
from Tarefas.db import SessionLocal
from sqlalchemy import exc
import logging

# Cria um logger
logger = logging.getLogger("logfile.log")

router = APIRouter()

@router.get(
    path='/tarefa/',
    response_model=Schema.list_tarefas_schema,
)
async def get_all_tarefas():
    '''
        Pego todos os itens da coluna 'tarefa' do banco,
            retornando uma lista de dicionarios contendo os dados das tarefas
            no corpo da resposta
        
        Caso algum erro ocorra é retornado um codigo 500,
            no corpo temos 'error' com uma mensagem do que foi o erro
    '''
    logger.info("GET /tarefa/")
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
            logger.debug(str(e))
            response = {"error": "Internal Error"}
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
    '''
        Obtem todas as informações de uma tarefa especica
            busca tareca com id: 'id' e retorna um kson com seus dados
        :type id: int -> 'id' da tarefa desejada
    '''
    logger.info(f"GET /tarefa/{id}")
    session = SessionLocal()
    tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
    try:
        if not tarefa:
            logger.info(f"{id} Not Found")
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
    '''
        Deleta a tarefa com id especificado

        :type id: int -> 'id' da tarefa a ser deletada
    '''
    logger.info(f"DELETE /tarefa/{id}")
    session = SessionLocal()
    tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
    try:
        if not tarefa:
            logger.info(f"{id} Not Found")
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
    '''
        Cria uma nova tarefa
            os dados para criação da tarefa deve ser passada no corpo do request

        :type rbody: Schema.put_post_tarefa_schema -> json com dados da tarefa a ser criada
    '''
    logger.info(f"POST /tarefa/")
    session = SessionLocal()
    id = None
    try:
        print(rbody,type(rbody))
        tarefa = Tarefa(**dict(rbody))
        session.add(tarefa)
        session.flush()
        session.commit()
        id = tarefa.id
    except exc.SQLAlchemyError as e:
        logger.debug(str(e))
        status_code = status.HTTP_400_BAD_REQUEST
        response = {"error": "Problema nos dados fornecidos"}
        return JSONResponse(content=response, status_code=status_code)
    except Exception as ex:
        logger.debug(str(ex))
        response = {"error": 'Internal Error'}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=response, status_code=status_code)
    finally:
        session.close()
    return {"msg":"Tarefa criada com sucesso",'new_tarefa_id':id}

@router.put(
    path='/tarefa/{id}',
)
async def edit_tarefa(id:int,rbody: Schema.put_post_tarefa_schema):
    '''
        Edita um tarefa, com id 'id'
            os dados para edição da tarefa deve ser passada no corpo do request

        :type id: int -> id da tarefa que sera editada
        :type rbody: Schema.put_post_tarefa_schema -> json com todos os dados de uma tarefa, que sobreescreverao os valores antigos
    '''
    logger.info(f"PUT /tarefa/{id}")
    session = SessionLocal()
    tarefa = session.query(Tarefa).filter(Tarefa.id == id).first()
    if not tarefa:
        logger.info(f"{id} Not Found")
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
        logger.debug(str(e))
        status_code = status.HTTP_400_BAD_REQUEST
        response = {"error": "Problema nos dados fornecidos"}
        return JSONResponse(content=response, status_code=status_code)
    except Exception as ex:
        logger.debug(str(ex))
        response = {"error": 'Internal Error'}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=response, status_code=status_code)
    finally:
        session.close()
    return {"msg":"Tarefa criada com sucesso"}

# par quando tivermos um alta quantidade seria usado esse ao invez de get_all ( caso entenda que existe altas quantidades, esse seria o '/tarefa/')
@router.get(
    path='/tarefa/slice/{start}/{limit}',
    response_model=Schema.slice_tarefas_schema,
)
#Nao foi possivel deixa 'start' e 'limit' como query paramets fora da url pois, existe um problema de conversão ( nao estao convertendo str para int )
async def get_slice_tarefas(start:int,limit:int):
    '''
        Pega os itens entre 'start' e 'limit'+1
            retornando uma lista de dicionarios com dados das tarefas,
            usando uma versão simplificada de uma tarefa a qual possui
            id, titulo, data e estado
            essa lista tera até 'limit'-'start' itens, caso existam.
        
        Caso algum erro ocorra é retornado um codigo 500,
            no corpo temos 'error' com uma mensagem do que foi o erro

        :type start: int -> index do primeiro item a ser retornado
        :type limit: int -> index do ultimo item a ser retornado se existir
    '''
    logger.info(f"GET /tarefa/slice")
    try:
        start = int(start)
        limit = int(limit)
    except Exception as e:
        logger.debug(str(e))
        response = {"error": 'Start ou Limit não são numeros'}
        status_code = status.HTTP_400_BAD_REQUEST
        return JSONResponse(content=response, status_code=status_code)
    session = SessionLocal()
    response = {'tarefas':[]}
    try:
        tarefas = session.query(Tarefa).slice(start, limit+1).all()
        response['tarefas'] = [ 
                    {
                        "id":tarefa.id,
                        "titulo":tarefa.titulo,
                        'descricao':tarefa.descricao,
                        'data':tarefa.data,
                        'status':tarefa.status,
                    } for tarefa in tarefas
                  ]
        response['total'] = session.query(Tarefa).count()
    except Exception as e:
        logger.debug(str(e))
        response = {"error": 'Internal Error'}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return JSONResponse(content=response, status_code=status_code)
    finally:
        session.close()
    return response