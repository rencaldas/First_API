from fastapi import FastAPI
from pydantic import BaseModel
from app.api.v1 import auth, users, products

# Criação da aplicação FastAPI
app = FastAPI(title="Rencaldas's API")

# Registrar as rotas organizadas
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(products.router, prefix="/products", tags=["products"])

# Modelo de exemplo para testar POST
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# Rota GET raiz
@app.get("/")
def read_root():
    return {"message": "Olá! API rodando."}

# Rota GET com parâmetro
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Rota POST que recebe JSON
@app.post("/items")
def create_item(item: Item):
    return {"message": "Item recebido", "item": item}
