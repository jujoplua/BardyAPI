from pydantic import BaseModel

class Usuario(BaseModel):
    _id: str = None
    username: str = None
    password: str = None
    nombres: str = None
    apellidos: str = None
    email : str = None