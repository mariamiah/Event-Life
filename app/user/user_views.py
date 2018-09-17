from flask import Blueprint, request, jsonify, json
from app.models.user_model import User


guest = Blueprint('guest', __name__)

users = []


@guest.route('/api/add-user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        data = request.get_json()
        user = User(data['email'], data['firstname'], data['lastname'], data['password'])
        users.append(user)
    return jsonify(user.create_user()), 201


@guest.route('/api/delete-users/<lastname>', methods=['DELETE'])
def delete_user(lastname):
    for user in users:
        if user['lastname'] == lastname:
            users.remove(user)
    return jsonify({"message":users})


@guest.route('/api/get-users')
def get_users():
    Users = [user.create_user() for user in users]
    return jsonify({'message': Users})
