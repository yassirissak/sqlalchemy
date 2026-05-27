from flask import Blueprint,request, jsonify
from app import app, db
from models import User
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user_bp', __name__)




# ==================== USER =============================

# ADD
@user_bp.route("/users", methods=["POST"])
def add_users():
    data = request.get_json()

    new_user = User(
        username=data["username"],
        email=data["email"],
        password=generate_password_hash(data["password"])

    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": "User created successfully"}), 201


@user_bp.route("/users")
def fetch_users():
    users = User.query.all()

    results = []
    for user in users:
        results.append({
            "id": user.id,
            "username": user.username
        })

    return jsonify(results), 200


@user_bp.route("/users/<int:id>")
def fetch_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User does not exist"}), 404

    my_user = {
        "id": user.id,
        "username": user.username
    }
    return jsonify(my_user), 200


@user_bp.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User does not exist"}), 404

    data = request.get_json()

    user.username = data.get("username", user.username)

    db.session.commit()

    return jsonify({"success": "User updated successfully"}), 200


@user_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "The user you want to delete does not exist"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"success": "User deleted successfully"}), 200
