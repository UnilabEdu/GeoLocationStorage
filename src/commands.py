from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import User
from src.models.user import Role


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

    click.echo("Adding roles to database...")

    role1 = Role(name="user")
    role2 = Role(name="admin")

    db.session.add(role1)
    db.session.add(role2)

    db.session.commit()

    click.echo("Roles added to database.")

    click.echo("Adding users to database...")

    user1 = User(username="Username1234", password="Password1234", role_id=2)
    user2 = User(username="Dummy", password="Data", role_id=1)
    db.session.add(user1)
    db.session.add(user2)

    click.echo("Users added to database.")

    db.session.commit()

    click.echo("Database populated.")
