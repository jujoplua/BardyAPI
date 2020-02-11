import json
from bson import json_util
from fastapi import FastAPI

from db.usuarioModel import Usuario

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/usuarios")
async def getUsuarios():
    u = Usuario()
    users = list(u.getUsuarios())
    return json.loads(json.dumps(users, default=json_util.default))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='192.168.127.49', port=8000, workers=2)


