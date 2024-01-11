import unittest
from main import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.token = self.get_token()
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def get_token(self):
        data_login = {'username': 'Daniel', 'password': '123456'}
        response = self.app.post('/login', json=data_login, content_type='application/json')
        data = response.get_json()
        return data['access_token']

    def test_login(self):
        data = {'username': 'Daniel', 'password': '123456'}
        response = self.app.post('/login', json=data, content_type='application/json')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_token' in data)
        self.assertTrue(data['access_token'])

    # def test_register(self):
    #     data = {'username': 'Joao', 'password': '123456'}
    #     response = self.app.post('/register', json=data, content_type='application/json')
    #     data = response.get_json()
    #     self.assertEqual(response.status_code, 404)

    def test_update_product(self):
        code = '10975992'
        data = {
            'creator': 'Test'
        }

        response = self.app.put(f'products/{code}', json=data, headers=self.headers)
        self.assertIn(response.status_code, [200, 204])
        self.assertEqual(response.get_json(), {"message": 'Success'})

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_list_product_exist(self):
        code = '10975992'
        response = self.app.get(f'products/{code}', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_list_product_not_exist(self):
        code = '109759921111'
        response = self.app.get(f'products/{code}', headers=self.headers)
        self.assertEqual(response.status_code, 404)

    def test_list_all_products(self):
        response = self.app.get(f'products', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    # def test_delete_product(self):
    #     code = '7898901621249'
    #     response = self.app.delete(f'products/{code}', headers=self.headers)
    #     self.assertEqual(response.get_json(), {'message': 'product deleted successfully'})
    #     self.assertEqual(response.status_code,200)

    def test_auth(self):
        response = self.app.get('products/10975992')
        self.assertEqual(response.status_code,401)
        self.assertEqual(response.get_json(),{"msg": "Missing Authorization Header"})