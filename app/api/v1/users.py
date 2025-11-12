from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    email: str

# Banco de dados temporário na memória
users_db = []

@router.get("/")
def list_users():
    return users_db

@router.post("/")
def create_user(user: User):
    users_db.append(user)
    return {"message": "Usuário criado com sucesso!", "user": user}
