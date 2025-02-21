from flask import render_template, Blueprint, request
from os import path
from src.config import Config
from src.models.location import Location

TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "main")

main_blueprint = Blueprint("main", __name__, template_folder=TEMPLATES_FOLDER)

@main_blueprint.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 4
    pagination = Location.query.order_by(Location.id.desc()).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('index.html', locations=pagination.items, pagination=pagination)

@main_blueprint.route('/about-project')
def about():
    return render_template('about-project.html')
