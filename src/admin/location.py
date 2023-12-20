from flask_admin.model.template import LinkRowAction

from src.admin.base import SecureModelView
from src.models import LocationRelation, LocationConnection, Link


class LocationViewRowAction(LinkRowAction):
    def __init__(self, icon_class, url=None):
        super().__init__(icon_class, url)

    def render(self, context, row_id, row):
        m = self._resolve_symbol(context, 'row_actions.link')

        url = f"http://localhost5000/locations/{row.id}"

        return m(self, url)


class LocationView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ['name', "types"]

    form_columns = ["name", "period", "description", "latitude", "longitude", "types", "bibliographies"]

    column_searchable_list = ["name"]

    column_labels = {"name": "სახელი", "types": "ტიპი/ტიპები", "period": "დროის პერიოდი", "description": "აღწერა",
                     "latitude": "გრძედი", "longitude": "განედი"}

    column_sortable_list = ["name", ("types", "types.name")]

    column_extra_row_actions = [LocationViewRowAction("fa fa-eye")]

    inline_models = [LocationRelation, LocationConnection, Link]
