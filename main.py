import json
import hashlib
from bson import json_util
from fastapi import FastAPI

from db.usuarioModel import UsuarioModel
from entidades.usuario import Usuario

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/usuarios")
async def getUsuarios():
    u = UsuarioModel()
    users = list(u.getUsuarios())
    return json.loads(json.dumps(users, default=json_util.default))

@app.post("/api/usuarios/login")
async def getUsuarioPorUserPass(u: Usuario):
    user = UsuarioModel()
    passMD5 = hashlib.md5(u.password.encode('utf-8'))
    us = user.getUsuarioUserPass(u.username, passMD5.hexdigest() )
    return json.loads(json.dumps(us, default=json_util.default))

@app.post("/api/usuarios/crear")
async def crearUsuario(u: Usuario):
    user = UsuarioModel()
    passMD5 = hashlib.md5(u.password.encode('utf-8'))
    u.password = passMD5.hexdigest()
    us = user.crearUsuario(u)
    return json.loads(json.dumps(us, default=json_util.default))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='192.168.1.11', port=8000, workers=2, reload=True)


