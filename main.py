from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="CRUD Usuários", version="1.0.0")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permite todas origens (ou coloque só http://127.0.0.1:5500 por exemplo)
    allow_credentials=True,
    allow_methods=["*"],  # permite GET, POST, PUT, DELETE, OPTIONS...
    allow_headers=["*"],
)


# Modelo de usuário
class User(BaseModel):
    id: int
    name: str

# "Banco de dados" em memória
db: Dict[int, User] = {
    1: User(id=1, name="Maria"),
    2: User(id=2, name="João"),
}

@app.get("/users")
def list_users():
    return list(db.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db[user_id]

@app.post("/users", status_code=201)
def create_user(user: User):
    if user.id in db:
        raise HTTPException(status_code=400, detail="Usuário com esse ID já existe")
    db[user.id] = user
    return {"message": "Usuário criado com sucesso", "user": user}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db[user_id] = user
    return {"message": "Usuário atualizado com sucesso", "user": user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    deleted = db.pop(user_id)
    return {"message": "Usuário removido com sucesso", "user": deleted}
