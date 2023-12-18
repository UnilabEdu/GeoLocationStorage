from flask_admin import Admin
from flask_admin.form import rules
from wtforms.fields import SelectField

from src.admin.base import SecureModelView
from src.models import LocationConnection


class LocationView(SecureModelView):
    column_list = ['name', "types"]

    # TODO: ფორმა მაქვს გასასწორებელი, ისე როგორც, ტექნიკურ დავალებაშია მოცემული

    form_create_rules = [
        rules.FieldSet(("name", "period", "description", "latitude", "longitude", "types", "relations", "from_or_with", "connections_from", "connections_with", "bibliographies", "links"), "Location"),
    ]

    form_edit_rules = form_create_rules
