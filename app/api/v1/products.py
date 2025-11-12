from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Product(BaseModel):
    id: int
    name: str
    price: float

products_db = []

@router.get("/")
def list_products():
    return products_db

@router.post("/")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Produto criado com sucesso!", "product": product}
