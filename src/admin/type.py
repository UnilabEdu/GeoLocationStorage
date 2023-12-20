from src.admin.base import SecureModelView


class TypeView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ["name"]

    column_labels = {'name': "ადგილის ტიპი"}

    column_searchable_list = ["name"]
