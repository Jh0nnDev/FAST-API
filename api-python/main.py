from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from database import SessionLocal
import models

app = FastAPI()

class Tarefa(BaseModel):
    id: int
    titulo_tarefa: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tarefas", response_model=list[Tarefa])
def buscar_tarefas(db: Session = Depends(get_db)):
    tarefas = db.query(models.Tarefa).all()
    return tarefas

@app.post("/tarefas", response_model = Tarefa)
def criar_tarefa(tarefa: Tarefa, db: Session = Depends(get_db)):
    nova_tarefa = models.Tarefa(titulo_tarefa=tarefa.titulo_tarefa)
    db.add(nova_tarefa)
    db.commit()
    return nova_tarefa 

@app.put("/tarefas/{id}", response_model= Tarefa)
def atualizar_tarefa(id: int, tarefa:Tarefa, db: Session = Depends(get_db)):
    stmt =(
        update(models.Tarefa)
        .where(models.Tarefa.id == id)
        .values(titulo_tarefa=tarefa.titulo_tarefa)
    )
    db.execute(stmt)
    db.commit()
    return db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    
@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int, db: Session = Depends(get_db)):
    stmt = delete(models.Tarefa).where(models.Tarefa.id == id)
    db.execute(stmt)
    db.commit()
    return {"mensagem": "Tarefa deletada com sucesso!"}