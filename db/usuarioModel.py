from bson.py3compat import imap

from db.database import Database
from db.model import Model
from entidades.usuario import Usuario


class UsuarioModel(Model):
    nombre = "usuarios"
    collection = Database().get_collection(nombre)

    def getUsuarios(self):
        users = imap(UsuarioModel, UsuarioModel.collection.find())
        return users

    def getUsuarioUserPass(self, user:str, psw:str):
        return UsuarioModel.collection.find_one({"username": user, "password" : psw})

    def crearUsuario(self, user: Usuario):
        if(UsuarioModel.collection.find_one({"username": user.username}) == None):
            UsuarioModel.collection.save(user.dict())
            return UsuarioModel.collection.find_one({"username": user.username})
        else:
            return None