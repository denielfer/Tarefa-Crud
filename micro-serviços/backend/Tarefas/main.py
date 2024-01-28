# Applicação principal a ser chamada pelo uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Tarefas.views.tarefa import router as tarefa_router
from Tarefas.db import Base, engine
from Tarefas.setting import settings

app = FastAPI(title="Tarefas", version="1.0")
app.include_router(tarefa_router)
Base.metadata.create_all(bind=engine)

origins = [
    # settings.FRONTEND_URL
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
