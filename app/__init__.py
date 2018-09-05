from flask import Flask
from app.user.user_views import user

app = Flask(__name__)

app.register_blueprint(user)
