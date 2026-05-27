from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from models import Comment, Post

comment_bp = Blueprint("comment_bp", __name__)


# READ ALL COMMENTS
@comment_bp.route("/comments")
def fetch_comments():
    comments = Comment.query.all()

    results = []

    for comment in comments:
        results.append({
            "id": comment.id,
            "message": comment.message,
            "post_id": comment.post_id,
            "user_id": comment.user_id
        })

    return jsonify(results), 200


# CREATE COMMENT
@comment_bp.route("/comments", methods=["POST"])
@jwt_required()
def add_comment():
    data = request.get_json()

    current_user_id = get_jwt_identity()

    post = Post.query.get(data["post_id"])

    if not post:
        return jsonify({"error": "Post does not exist"}), 404

    new_comment = Comment(
        message=data["message"],
        post_id=data["post_id"],
        user_id=current_user_id
    )

    db.session.add(new_comment)
    db.session.commit()

    return jsonify({
        "success": "Comment created successfully",
        "comment": {
            "id": new_comment.id,
            "message": new_comment.message,
            "post_id": new_comment.post_id,
            "user_id": new_comment.user_id
        }
    }), 201


# READ ONE COMMENT
@comment_bp.route("/comments/<int:id>")
def fetch_comment(id):
    comment = Comment.query.get(id)

    if not comment:
        return jsonify({"error": "Comment does not exist"}), 404

    return jsonify({
        "id": comment.id,
        "message": comment.message,
        "post_id": comment.post_id,
        "user_id": comment.user_id
    }), 200


# UPDATE COMMENT
@comment_bp.route("/comments/<int:id>", methods=["PUT"])
@jwt_required()
def update_comment(id):
    comment = Comment.query.get(id)

    if not comment:
        return jsonify({"error": "Comment does not exist"}), 404

    current_user_id = get_jwt_identity()

    # check owner
    if comment.user_id != current_user_id:
        return jsonify({
            "error": "You are not allowed to update this comment"
        }), 403

    data = request.get_json()

    # VALIDATE POST
    if "post_id" in data:
        post = Post.query.get(data["post_id"])

        if not post:
            return jsonify({"error": "Post does not exist"}), 404

        comment.post_id = data["post_id"]

    comment.message = data.get("message", comment.message)

    db.session.commit()

    return jsonify({
        "success": "Comment updated successfully",
        "comment": {
            "id": comment.id,
            "message": comment.message,
            "post_id": comment.post_id,
            "user_id": comment.user_id
        }
    }), 200


# DELETE COMMENT
@comment_bp.route("/comments/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_comment(id):
    comment = Comment.query.get(id)

    if not comment:
        return jsonify({
            "error": "The comment you want to delete does not exist"
        }), 404

    current_user_id = get_jwt_identity()

    if comment.user_id != current_user_id:
        return jsonify({
            "error": "You are not allowed to delete this comment"
        }), 403

    db.session.delete(comment)
    db.session.commit()

    return jsonify({
        "success": "Comment deleted successfully"
    }), 200
