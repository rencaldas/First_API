from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha API simples")

# Modelo para requisições POST
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
