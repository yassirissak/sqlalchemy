from datetime import datetime
from datetime import timezone
from flask import Blueprint,request, jsonify
from app import  db
from models import User, TokenBlocklist
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt

auth_bp = Blueprint('auth_bp', __name__)




# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        # create access token
        access_token = create_access_token(identity=str(user.id) )
        refresh_token = create_refresh_token(identity=str(user.id) )
        return jsonify({"access_token": access_token, "refresh_token":refresh_token}), 200
    else:
        return jsonify({"error": "Wrong credentials"}), 401


# REFRESH AUTH TOKEN
@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    # get user id from the refresh token 
    current_user_id = get_jwt_identity()

    # token - short-lived
    access_token = create_access_token(identity=str(current_user_id))
    return jsonify({"access_token": access_token}), 200


# FETCH CURRENT USER
@auth_bp.route("/current_user", methods=["GET"])
@jwt_required()
def loggedin_user():
    current_user_id = get_jwt_identity()

    # fetch the user
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"error": "user doesn't exist"}), 404
    
    user_data = {
        "id":user.id,
        "email": user.email,
        "username": user.username
    }
    return jsonify(user_data), 200



# Logout
@auth_bp.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(jti=jti, created_at=now))
    db.session.commit()
    return jsonify({"success":"JWT revoked"}),401