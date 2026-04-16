from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Tarefa(BaseModel):
    id: int
    titulo_tarefa: str

@app.get("/tarefas", response_model=list[Tarefa])
def inicio():
    return [
            {"id": 1, "titulo_tarefa": "Comprar leite"},
            {"id": 2, "titulo_tarefa": "Jogar lixo fora"},
            {"id": 3, "titulo_tarefa": "Fazer feira"}
    ]

        