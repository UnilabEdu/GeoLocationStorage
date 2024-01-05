from src.admin.base import SecureModelView


class ConnectionView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ["name"]

    form_columns = ["name"]

    form_excluded_columns = ["locations"]

    column_labels = {"name": "კავშირის ტიპი"}

    column_searchable_list = ["name"]
