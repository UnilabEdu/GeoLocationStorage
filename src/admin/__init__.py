from flask_admin import Admin

from src.admin.base import SecureIndexView


admin = Admin(index_view=SecureIndexView(), name="Geolocation Storage", template_mode="bootstrap4")
