from sqlalchemy import Column, Integer, String
from database import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo_tarefa = Column(String(100))