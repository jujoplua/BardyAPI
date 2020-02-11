from bson.py3compat import imap

from db.database import Database
from db.model import Model


class Usuario(Model):
    nombre = "usuarios"
    collection = Database().get_collection(nombre)

    def getUsuarios(self):
        users = imap(Usuario, Usuario.collection.find())
        return users
