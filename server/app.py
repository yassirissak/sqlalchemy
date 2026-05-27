from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# JWT conf
from flask_jwt_extended import JWTManager
app.config["JWT_SECRET_KEY"] = "fyujvkyxbhvfjnxfgdbvkx,jvxhjbkjmhv"  # Change this!
jwt = JWTManager(app)


# the time for token to expired - jwt

# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USE_SSL"] = False

# app.config["MAIL_USERNAME"] = "kk@gmail.com"
# app.config["MAIL_PASSWORD"] = "ydsd dfgd dfdf dfdf"

# mail = Mail(app)

CORS(app)
app.secret_key = "sehtrsdyhndtejdydunuyehbdrvteryhe"

# models
import models

# views
from views import *


# REgistering Blueprints
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)
app.register_blueprint(auth_bp)



# Callback function to check if a JWT exists in the database blocklist
from models import TokenBlocklist

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None

# export FLASK_APP=app.py
# export FLASK_DEBUG=1
