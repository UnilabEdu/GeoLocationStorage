from flask_admin.model.template import LinkRowAction, EditPopupRowAction
from flask_admin.model import InlineFormAdmin
from wtforms.validators import DataRequired
from wtforms.fields import StringField

from src.admin.base import SecureModelView
from src.models import LocationRelation, LocationConnection, Link


class LocationViewRowAction(LinkRowAction):
    def __init__(self, icon_class, url=None):
        super().__init__(icon_class, url)

    def render(self, context, row_id, row):
        m = self._resolve_symbol(context, 'row_actions.link')

        url = f"http://localhost5000/locations/{row.id}"

        return m(self, url)


class InlineRelationView(InlineFormAdmin):
    form_args = {"period": {"validators": [DataRequired()]}}

    column_labels = {"name": "სახელი", "period": 'პერიოდი', "text": "ტექსტური ველი"}


class InlineConnectionView(InlineFormAdmin):
    form_args = {"location_with": {"validators": [DataRequired()]}, "connection_type": {"validators": [DataRequired()]}}

    column_labels = {"location_with": "ადგილის სახელი", "connection_type": "კავშირის ტიპი"}


class InlineLinkView(InlineFormAdmin):
    form_args = {"title": {"validators": [DataRequired()]}, "link": {"validators": [DataRequired()]}}

    column_labels = {"title": "ბმულის სახელი", "link": "ბმული"}


class LocationView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ['name', "types"]

    form_columns = ["name", "period", "description", "latitude", "longitude", "types", "bibliographies"]

    # Dictionary comprehension: Assigns each form_columns' DataRequired() Validator
    form_args = {key: {"validators": [DataRequired()]} for key in form_columns}

    column_searchable_list = ["name"]

    column_labels = {"name": "სახელი", "types": "ტიპი/ტიპები", "period": "დროის პერიოდი", "description": "აღწერა",
                     "latitude": "გრძედი", "longitude": "განედი", "bibliographies": "ბიბლიოგრაფია", "relations": "დაკავშირებული სახელები", "connections_from": "დაკავშირებული ადგილები", "links": "ბმული/ბმულები"}

    column_sortable_list = ["name", ("types", "types.name")]

    column_extra_row_actions = [LocationViewRowAction("fa fa-eye")]

    inline_models = [InlineRelationView(LocationRelation), InlineConnectionView(LocationConnection), InlineLinkView(Link)]
