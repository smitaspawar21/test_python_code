from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

# Mock user data for demonstration purposes
users = {
    "user1": "password1",
    "user2": "password2"
}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"message": "Login successful", "username": username}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401