from flask import Flask

from src.models import db, User, LocationConnection
from src.config import Config
from src.commands import init_db, populate_db
from src.extensions import migrate, login_manager
from src.admin import admin


COMMANDS = [
    init_db,
    populate_db
]


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/")
    def testing_purposes():
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


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)
