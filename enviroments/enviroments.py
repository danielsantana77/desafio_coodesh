import os
from dotenv import load_dotenv


class Enviroments:
    def __init__(self):
        load_dotenv()
        self.jwt_secret_key = os.getenv('JWT_SECRET_KEY')
        self.user = str(os.getenv('MONGO_ROOT_USERNAME'))
        self.password = str(os.getenv('MONGO_ROOT_PASSWORD'))
