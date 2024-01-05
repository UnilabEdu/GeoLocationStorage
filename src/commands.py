from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import User, Location, Type, LocationType, LocationRelation, ConnectionType, LocationConnection, \
    Bibliography, LocationBibliography, Link
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

    role1 = Role("user")
    role2 = Role("admin")

    role1.create(commit=False)
    role2.create(commit=False)

    db.session.commit()

    click.echo("Roles added to database.")

    click.echo("Adding users to database...")

    user1 = User("Username1234", "Password1234", 2)
    user2 = User("Dummy", "Data", 1)

    user1.create(commit=False)
    user2.create(commit=False)

    click.echo("Users added to database.")

    click.echo("Adding locations to database...")

    location1 = Location("Gonio")
    location2 = Location("Gonio Fortress")
    location3 = Location("Qartvlis Deda")

    location1.create(commit=False)
    location2.create(commit=False)
    location3.create(commit=False)

    click.echo("Adding location types to database...")

    type1 = Type("City")
    type2 = Type("Statue")
    type3 = Type("Fortress")

    type1.create(commit=False)
    type2.create(commit=False)
    type3.create(commit=False)

    LocationType(location1.id, type1.id).create(commit=False)
    LocationType(location2.id, type3.id).create(commit=False)
    LocationType(location3.id, type2.id).create(commit=False)

    click.echo("Location types added to database.")

    click.echo("Adding location relations to database...")

    LocationRelation(location1.id, "Gonio").create(commit=False)
    LocationRelation(location1.id, "Afsarut").create(commit=True)

    LocationRelation(location2.id, "Gonio Fortress").create(commit=False)
    LocationRelation(location2.id, "Afsarus").create(commit=True)

    LocationRelation(location3.id, "Qartvlis Deda").create(commit=False)

    click.echo("Location relations added to database.")

    click.echo("Adding location connections to database...")

    connection_type1 = ConnectionType("located at")
    connection_type2 = ConnectionType("located near")
    connection_type3 = ConnectionType("connection")

    connection_type1.create(commit=False)
    connection_type2.create(commit=False)
    connection_type3.create(commit=False)

    LocationConnection(location2.id, location1.id, connection_type1.id).create(commit=False)

    click.echo("Location connections added to database.")

    click.echo("Adding bibliographies to database...")

    bibliography1 = Bibliography("ABC")
    bibliography2 = Bibliography("DEF")
    bibliography3 = Bibliography("GHI")

    bibliography1.create(commit=False)
    bibliography2.create(commit=False)
    bibliography3.create(commit=False)

    LocationBibliography(location1.id, bibliography3.id).create(commit=False)
    LocationBibliography(location1.id, bibliography1.id).create(commit=False)

    click.echo("Bibliographies added to database.")

    click.echo("Adding links to database")

    link1 = Link(location1.id, "გონიო",
                 "https://ka.wikipedia.org/wiki/%E1%83%92%E1%83%9D%E1%83%9C%E1%83%98%E1%83%9D").create(
        commit=False)
    link2 = Link(location2.id, "გონიოს ციხე",
                 "https://ka.wikipedia.org/wiki/%E1%83%92%E1%83%9D%E1%83%9C%E1%83%98%E1%83%9D%E1%83%A1_%E1%83%AA%E1%83%98%E1%83%AE%E1%83%94",
                 ).create(commit=False)
    link3 = Link(location3.id, "ქართვლის დედა",
                 "https://ka.wikipedia.org/wiki/%E1%83%A5%E1%83%90%E1%83%A0%E1%83%97%E1%83%95%E1%83%9A%E1%83%98%E1%83%A1_%E1%83%93%E1%83%94%E1%83%93%E1%83%90",
                 ).create(commit=False)

    click.echo("Links added to database.")

    click.echo("Locations added to database.")

    db.session.commit()

    click.echo("Database populated.")
