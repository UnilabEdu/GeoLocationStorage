from flask.cli import with_appcontext
import click

from src.extensions import db
from src.models import User, Location, Type, LocationType, LocationRelation, ConnectionType, LocationConnection, \
    Bibliography, LocationBibliography, Link, LocationLink
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

    role1.create(commit=False)
    role2.create(commit=False)

    db.session.commit()

    click.echo("Roles added to database.")

    click.echo("Adding users to database...")

    user1 = User(username="Username1234", password="Password1234", role_id=2)
    user2 = User(username="Dummy", password="Data", role_id=1)

    user1.create(commit=False)
    user2.create(commit=False)

    click.echo("Users added to database.")

    click.echo("Adding locations to database...")

    location1 = Location(name="Gonio")
    location2 = Location(name="Gonio Fortress")
    location3 = Location(name="Qartvlis Deda")

    location1.create(commit=False)
    location2.create(commit=False)
    location3.create(commit=False)

    click.echo("Adding location types to database...")

    type1 = Type(name="City")
    type2 = Type(name="Statue")
    type3 = Type(name="Fortress")

    type1.create(commit=False)
    type2.create(commit=False)
    type3.create(commit=False)

    LocationType(location_id=location1.id, type_id=type1.id).create(commit=False)
    LocationType(location_id=location2.id, type_id=type3.id).create(commit=False)
    LocationType(location_id=location3.id, type_id=type2.id).create(commit=False)

    click.echo("Location types added to database.")

    click.echo("Adding location relations to database...")

    LocationRelation(location_id=location1.id, name="Gonio").create(commit=False)
    LocationRelation(location_id=location1.id, name="Afsarut").create(commit=True)

    LocationRelation(location_id=location2.id, name="Gonio Fortress").create(commit=False)
    LocationRelation(location_id=location2.id, name="Afsarus").create(commit=True)

    LocationRelation(location_id=location3.id, name="Qartvlis Deda").create(commit=False)

    click.echo("Location relations added to database.")

    click.echo("Adding location connections to database...")

    connection_type1 = ConnectionType(name="located at")
    connection_type2 = ConnectionType(name="located near")
    connection_type3 = ConnectionType(name="connection")

    connection_type1.create(commit=False)
    connection_type2.create(commit=False)
    connection_type3.create(commit=False)

    LocationConnection(located_from_id=location2.id, located_with_id=location1.id,
                       connection_type_id=connection_type1.id).create(commit=False)

    click.echo("Location connections added to database.")

    click.echo("Adding bibliographies to database...")

    bibliography1 = Bibliography(abbreviation="ABC")
    bibliography2 = Bibliography(abbreviation="DEF")
    bibliography3 = Bibliography(abbreviation="GHI")

    bibliography1.create(commit=False)
    bibliography2.create(commit=False)
    bibliography3.create(commit=False)

    LocationBibliography(location_id=location1.id, bibliography_id=bibliography3.id).create(commit=False)
    LocationBibliography(location_id=location1.id, bibliography_id=bibliography1.id).create(commit=False)


    click.echo("Bibliographies added to database.")

    click.echo("Adding links to database")

    link1 = Link(title="გონიო",
                 link="https://ka.wikipedia.org/wiki/%E1%83%92%E1%83%9D%E1%83%9C%E1%83%98%E1%83%9D")
    link2 = Link(title="გონიოს ციხე",
                 link="https://ka.wikipedia.org/wiki/%E1%83%92%E1%83%9D%E1%83%9C%E1%83%98%E1%83%9D%E1%83%A1_%E1%83%AA%E1%83%98%E1%83%AE%E1%83%94")
    link3 = Link(title="ქართვლის დედა",
                 link="https://ka.wikipedia.org/wiki/%E1%83%A5%E1%83%90%E1%83%A0%E1%83%97%E1%83%95%E1%83%9A%E1%83%98%E1%83%A1_%E1%83%93%E1%83%94%E1%83%93%E1%83%90")

    link1.create(commit=False)
    link2.create(commit=False)
    link3.create(commit=False)

    LocationLink(location_id=location1.id, link_id=link1.id).create(commit=False)
    LocationLink(location_id=location2.id, link_id=link2.id).create(commit=False)
    LocationLink(location_id=location3.id, link_id=link3.id).create(commit=False)

    click.echo("Links added to database.")

    click.echo("Locations added to database.")

    db.session.commit()

    click.echo("Database populated.")
