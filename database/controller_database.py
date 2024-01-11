import traceback

from .database import Database
from csv_data.reader import ReadCSV


class Controller:

    def __init__(self):
        self.__database = None
        self.connection()

    def insert_user(self, user):
        return self.__database.insert_user(user)

    def find_user(self, user):
        data = self.__database.find_user(user)
        if data: return data
        return None

    def insert_products(self, products):
        return self.__database.insert_one(products)

    def insert_many_products(self, list_products):
        self.__database.insert_many(list_products)

    def find_all_products(self, ):
        return self.__database.find_all()

    def find_products(self, products):
        data = self.__database.find_one(products)
        if data: return data
        return None

    def update_product(self, code, data):
        return self.__database.update_one(code, data)

    def delete_product(self, code):
        return self.__database.delete_one(code)

    def verify_connection(self):
        try:
            self.__database = Database()
            self.__database.client.list_database_names()
            return True
        except:
            return False

    def connection(self):
        try:
            db = Database()
            if 'open_food_fact' in db.client.list_database_names():
                db_collections = db.client['open_food_fact'].list_collection_names()
                if not 'products' in db_collections:
                    db.client['open_food_fact'].create_collection('products')
                if not 'users' in db_collections:
                    db.client['open_food_fact'].create_collection('users')
                self.__database = db
                return
            products = ReadCSV().products
            db.insert_many(products)
            self.__database = db
            return
        except:
            print(traceback.print_exc())
            return
