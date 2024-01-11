from flask import Flask, jsonify, request
from database.controller_database import Controller
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from enviroments import env
from datetime import datetime, timedelta
import time


controller_db = Controller()
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = env.jwt_secret_key
jwt = JWTManager(app)
time_init = time.time()


@app.route('/')
def index():
    response = {}
    response['BD_connection'] = controller_db.verify_connection()
    response['message'] = 'The app is running'
    response['time'] = str((time.time() - time_init)/ 60)[:4] + ' minutes'
    return jsonify(response), 200


@app.route('/products')
@jwt_required()
def list_products():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))

    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    products = controller_db.find_all_products()
    paginated_items = products[start_index:end_index]

    return jsonify(
        {'products': paginated_items, 'total_products': len(products), 'page': page, 'per_page': per_page}), 200


@app.route('/products/<code>', methods=['GET'])
@jwt_required()
def list_product_by_code(code):
    product = controller_db.find_products(code)
    if not product:
        return jsonify({'message': 'product not found'}), 404
    return jsonify(product)


@app.route('/products/<code>', methods=['DELETE'])
@jwt_required()
def delete_product(code):
    product = controller_db.delete_product(code)
    if not product:
        return jsonify({'message': 'product not found'}), 404
    return jsonify({'message': 'product deleted successfully'}), 200


@app.route('/products/<code>', methods=['PUT'])
@jwt_required()
def update_product(code):
    if not request.json:
        return jsonify({"message": 'Body empty'}), 400

    data = request.json
    response = controller_db.update_product(code, data)
    if not response:
        return jsonify({'message': 'product not found'}), 404

    return jsonify({"message": 'Success'}), 200


@app.route('/register', methods=['POST'])
def register():
    if not request.json:
        return jsonify({"message": 'Body empty'}), 400

    data = request.json
    response = controller_db.insert_user(data)
    if not response:
        return jsonify({'message': 'User Already Exists'}), 404

    return jsonify({"message": 'Success'}), 200


@app.route('/login', methods=['POST'])
def login():
    if not request.json:
        return jsonify({"message": 'Body empty'}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    data = {'username': username, 'password': password}

    response = controller_db.find_user(data)
    if not response:
        return jsonify({'message': 'Incorrect Credentials'}), 404

    expiration = timedelta(hours=1)
    access_token = create_access_token(identity=username, expires_delta=expiration)
    return jsonify(access_token=access_token), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
