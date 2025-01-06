from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/data', methods=['GET'])
def get_user_data():
    # Sample user data
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "mobile": "123-456-7890"
    }
    return jsonify(user_data)