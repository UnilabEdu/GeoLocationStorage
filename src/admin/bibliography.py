from wtforms.validators import DataRequired

from src.admin.base import SecureModelView


class BibliographyView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ["abbreviation", "author", "title", "publisher", "year", "location", "language", "comment"]

    form_excluded_columns = ["locations"]

    column_labels = {"abbreviation": "აბრევიაცია", "author": "ავტორი", "publisher": "გამომცემლობა", "title": "სათაური",
                     "year": "გამოცემის წელი", "location": 'გამოცემის ადგილი', 'comment': "კომენტარის ველი", "language": "ენა"}

    form_args = {key: {"validators": [DataRequired()]} for key in column_list}

    column_searchable_list = ["abbreviation", "author", "title", "publisher", "year", "location", "language", "comment"]
