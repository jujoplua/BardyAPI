from pymongo import MongoClient


class Database:

    def __init__(self) -> object:
        MONGO_URI = 'mongodb://admin:admin@localhost:27017/bardy'
        self._url = MONGO_URI
        self._client = MongoClient(self._url);
        self.__database = 'bardy'

    def get_database(self):
        return self._client.get_database(self.__database)

    def get_collection(self, name: str):
        return self.get_database().get_collection(name)

    def findAll(self, name: str):
        return self.get_collection(name).find()

