from src.admin.base import SecureModelView


class BibliographyView(SecureModelView):
    edit_modal = True
    create_modal = True

    column_list = ["abbreviation", "author", "title", "publisher", "year", "location", "language", "comment"]

    column_labels = {"abbreviation": "აბრევიაცია", "author": "ავტორი", "publisher": "გამომცემლობა", "title": "სათაური",
                     "year": "გამოცემის წელი", "location": 'გამოცემის ადგილი', 'comment': "კომენტარის ველი", "language": "ენა"}

    column_searchable_list = ["abbreviation", "author", "title", "publisher", "year", "location", "language", "comment"]
