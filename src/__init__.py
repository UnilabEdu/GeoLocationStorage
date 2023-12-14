from flask import Flask
from flask_login import login_user

from src.models import db, User, Location, Type, ConnectionType, Bibliography
from src.config import Config
from src.commands import init_db, populate_db
from src.extensions import migrate, login_manager
from src.admin import admin
from src.admin.base import SecureModelView
from src.admin.location import LocationView


COMMANDS = [
    init_db,
    populate_db
]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/")
    def testing_purposes():
        login_user(User.query.get(1))
        return "Hello World!"

    register_extensions(app)
    register_commands(app)

    return app


def register_extensions(app):

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app, db)

    # Flask-Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get_or_404(user_id)

    # Flask-Admin
    admin.init_app(app)
    admin.add_view(LocationView(Location, db.session, name="ადგილები", endpoint="location"))
    admin.add_view(SecureModelView(Type, db.session, name="ადგილის ტიპები", endpoint="types"))
    admin.add_view(SecureModelView(ConnectionType, db.session, name="კავშირის ტიპი", endpoint="connection_type"))
    admin.add_view(SecureModelView(Bibliography, db.session, name="წყარო/ბიბლიოგრაფია", endpoint="bibliography"))


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
