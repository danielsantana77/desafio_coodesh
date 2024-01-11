from pymongo import MongoClient
from datetime import datetime
from enviroments import env


class Database:

    def __init__(self):
        self.user = env.user
        self.password = env.password
        self.client = MongoClient(username=self.user,
                                  password=self.password,
                                  host='mongodb', timeoutMS=5000)

        self.db = self.client['open_food_fact']
        self.products_collection = self.db['products']
        self.users_collection = self.db['users']

    def insert_user(self, data):
        filter = {'username': data['username']}
        if self.users_collection.find_one(filter): return None
        result = self.users_collection.insert_one(data)
        return result

    def find_user(self, data):
        projection = {'_id': 0}
        username = data['username']
        password = data['password']
        filter = {'username': username, 'password': password}
        documents = self.users_collection.find(filter, projection)
        return self.__documents_to_json(documents)

    def insert_one(self, data):
        filter = {'code': data['code']}
        if self.products_collection.find_one(filter): return None
        data['created_t'] = datetime.now().timestamp() * 1000
        data['last_modified_t'] = datetime.now().timestamp() * 1000
        result = self.products_collection.insert_one(data)
        return result

    def insert_many(self, list_data):
        self.products_collection.insert_many(list_data)

    def find_all(self):
        filter = {'status': 'published'}
        documents = self.products_collection.find(filter)
        return self.__documents_to_json(documents)

    def find_one(self, data):
        projection = {'_id': 0}
        filter = {'code': data, 'status': 'published'}
        documents = self.products_collection.find(filter, projection)
        return self.__documents_to_json(documents)

    def update_one(self, code, data):
        if not self.find_one(code): return None
        filter = {'code': code}
        data = data
        data['last_modified_t'] = datetime.now().timestamp() * 1000
        set = {'$set': data}
        return self.products_collection.update_one(filter, update=set, upsert=False)

    def delete_all(self):
        self.products_collection.delete_many({})

    def delete_one(self, code):
        if not self.find_one(code): return None
        data = {'status': 'trash'}
        return self.update_one(code, data)

    def __documents_to_json(self, documents):
        doc = []
        for document in documents:
            if '_id' in document.keys():
                document['_id'] = str(document['_id'])
            doc.append(document)

        return doc

# print(Database().client.list_database_names())
