from flask_admin import Admin
from flask_admin.form import rules
from wtforms.fields import SelectField

from src.admin.base import SecureModelView


class LocationView(SecureModelView):
    column_list = ['name', "types"]

    form_extra_fields = {
        "from_or_with": SelectField("Connection", choices=["From", "With"])
    }

    # TODO: I have to make form as it is in Tech work

    form_create_rules = [
        rules.FieldSet(("name", "period", "description", "latitude", "longitude", "types", "relations", "from_or_with", "connection_from"), "Location"),
    ]

    form_edit_rules = form_create_rules
