from flask import render_template, Blueprint
from os import path
from src.config import Config
TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "pages")

pages_bp = Blueprint("pages", __name__, template_folder=TEMPLATES_FOLDER)

@pages_bp.route('/list_of_places')
def locations():
    return render_template('list_of_places.html')


@pages_bp.route('/bibliography')
def bibliography():
    return render_template('bibliography.html')