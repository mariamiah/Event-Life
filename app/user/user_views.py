from flask import Blueprint, request, jsonify, json
from app.models.user_model import User

user = Blueprint('user', __name__)

users = []


@user.route('/api/add-user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        data = request.get_json()
        user = User(data['email'], data['firstname'], data['lastname'], data['password'])
        users.append(user)
    return jsonify(user.create_user()), 201


@user.route('/api/delete-users', methods=['DELETE'])
def delete_user():
    del users
    return jsonify({'message': "Successfully deleted"}), 200


@user.route('/api/get-users')
def get_users():
    Users = [user.create_user() for user in users]
    return jsonify({'message': Users})
