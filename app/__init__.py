from flask import Flask
from app.user.user_views import guest


app = Flask(__name__)

app.register_blueprint(guest)


