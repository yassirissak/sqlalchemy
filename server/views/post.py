
from flask import Flask, request, jsonify
from app import app, db
from models import Post, User, Comment

# ==================================== CRUD POST ================================================================
# READ
@app.route("/posts")
def fetch_posts():
    # fetching data in sqlalchemy
    posts = Post.query.all()
    
    results = []

    for post in posts:
        results.append({
            "id":post.id,
            "title": post.title,
            "content": post.content
            }
        )
    return jsonify(results), 200

# ADD
@app.route("/posts", methods=["POST"])
def add_post():
    data = request.get_json()

    user = User.query.get(data["user_id"])
    if not user:
        return jsonify({"error": "Unauthorized as user do not exist"}), 404
    
    new_post = Post(
        title=data["title"],
        content=data["content"],
        user_id=data["user_id"]
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({"success": "Post created successfully"}), 201


# read one post
@app.route("/posts/<int:post_id>")
def fetch_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post does not exists"}), 404
    
    my_post = {
        "id": post.id,
        "title": post.title,
        "content": post.content
    }
    return jsonify(my_post), 200


# -0---UPDATE
@app.route("/posts/<int:id>", methods=["PUT"])
def update_post(id):
    # fetch the post
    post = Post.query.get(id)
    # if post doesn't exists give an error
    if not post:
        return jsonify({"error": "Post does not exists"}), 404
    

    data = request.get_json()

    post.title = data.get("title", post.title)
    post.content = data.get("content", post.content)

    db.session.commit()

    return jsonify({"success": "Post updated successfully"}), 200


# DELETE
@app.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    # fetch the post
    post = Post.query.get(id)
    # if post doesn't exists give an error
    if not post:
        return jsonify({"error": "The post you want to delete does not exists"}), 404

    db.session.delete(post)
    db.session.commit()

    return jsonify({"success": "Post deleted successfully"}), 200



# ==================== USER =============================

# ADD
@app.route("/users", methods=["POST"])
def add_users():
    data = request.get_json()
    
    new_user = User(
        username=data["username"],
      
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": "User created successfully"}), 201


@app.route("/users")
def fetch_users():
    users = User.query.all()

    results = []
    for user in users:
        results.append({
            "id": user.id,
            "username": user.username
        })

    return jsonify(results), 200


@app.route("/users/<int:id>")
def fetch_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User does not exist"}), 404

    my_user = {
        "id": user.id,
        "username": user.username
    }
    return jsonify(my_user), 200


@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User does not exist"}), 404

    data = request.get_json()

    user.username = data.get("username", user.username)

    db.session.commit()

    return jsonify({"success": "User updated successfully"}), 200


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "The user you want to delete does not exist"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"success": "User deleted successfully"}), 200



# ==================== COMMENT =============================

@app.route("/comments")
def fetch_comments():
    comments = Comment.query.all()

    results = []
    for comment in comments:
        results.append({
            "id": comment.id,
            "message": comment.message,
            "post_id": comment.post_id
        })

    return jsonify(results), 200


@app.route("/comments", methods=["POST"])
def add_comment():
    data = request.get_json()

    post = Post.query.get(data["post_id"])
    if not post:
        return jsonify({"error": "Post does not exist"}), 404

    new_comment = Comment(
        message=data["message"],
        post_id=data["post_id"]
    )

    db.session.add(new_comment)
    db.session.commit()

    return jsonify({"success": "Comment created successfully"}), 201


@app.route("/comments/<int:id>")
def fetch_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"error": "Comment does not exist"}), 404

    my_comment = {
        "id": comment.id,
        "message": comment.message,
        "post_id": comment.post_id
    }
    return jsonify(my_comment), 200


@app.route("/comments/<int:id>", methods=["PUT"])
def update_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"error": "Comment does not exist"}), 404

    data = request.get_json()

    if "post_id" in data:
        post = Post.query.get(data["post_id"])
        if not post:
            return jsonify({"error": "Post does not exist"}), 404
        comment.post_id = data["post_id"]

    comment.message = data.get("message", comment.message)

    db.session.commit()

    return jsonify({"success": "Comment updated successfully"}), 200


@app.route("/comments/<int:id>", methods=["DELETE"])
def delete_comment(id):
    comment = Comment.query.get(id)
    if not comment:
        return jsonify({"error": "The comment you want to delete does not exist"}), 404

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"success": "Comment deleted successfully"}), 200
