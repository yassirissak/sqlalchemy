from app import db

# MODELS
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), nullable=True)

    posts = db.relationship("Post", backref='user')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id") )

    comments = db.relationship("Comment", backref='post')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))



class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
