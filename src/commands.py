from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import User


@click.command("init-db")
@with_appcontext
def init_db():
    click.echo("Creating database tables...")
    db.drop_all()
    db.create_all()
    click.echo("Database created.")


@click.command("populate-db")
def populate_db():
    click.echo("Populating database...")
    user1 = User(username="Username1234", password="Password1234")
    user2 = User(username="Dummy", password="Data")
    db.session.add(user1)
    db.session.add(user2)

    click.echo("Users added to database")

    db.session.commit()

    click.echo("Database populated.")
