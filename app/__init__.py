from flask import Flask
from .config import Configuration
from .routes import orders, session
from .models import db, Employee
from flask_login import LoginManager
import os
app = Flask(__name__)
app.config.from_object(Configuration)
# update= {
#     'SECRET_KEY': os.environ.get('SECRET_KEY'),
#     'SQLALCHEMY_TRACK_MODIFICATIONS' : False,
#     'SQLALCHEMY_DATABASE_URI' :os.environ.get("DATABASE_URL")
# }
# app.config.update(update)
app.register_blueprint(orders.bp)
app.register_blueprint(session.bp)

db.init_app(app)

login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
