from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Modelo de usuário para login/cadastro
class User(BaseModel):
    username: str
    password: str

# Simulação de login
@router.post("/login")
def login(user: User):
    if user.username == "admin" and user.password == "123":
        return {"message": "Login bem-sucedido!"}
    return {"error": "Credenciais inválidas"}

# Simulação de cadastro
@router.post("/register")
def register(user: User):
    return {"message": f"Usuário {user.username} cadastrado com sucesso!"}
