from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
  return {"Hello": "World"}

@app.get('/items/{item_id}')
def getItem(item_id: int, q: Optional[str] = None):
  return {"item_id": item_id, "q": q}