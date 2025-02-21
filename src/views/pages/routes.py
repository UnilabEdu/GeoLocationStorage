from flask import render_template, Blueprint, request
from os import path
from src.config import Config
from src.models.bibliography import Bibliography
from src.models import Location


TEMPLATES_FOLDER = path.join(Config.BASE_DIRECTORY, "templates", "pages")

pages_bp = Blueprint("pages", __name__, template_folder=TEMPLATES_FOLDER)

@pages_bp.route('/bibliography')
def bibliography():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    bibliographies = Bibliography.query.order_by(Bibliography.id.desc()).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('bibliography.html', bibliographies=bibliographies)


@pages_bp.route('/list_of_places')
def locations():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    pagination = Location.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('list_of_places.html', locations=pagination.items, pagination=pagination)


@pages_bp.route('/place/<int:location_id>')
def place_detail(location_id):
    location = Location.query.get_or_404(location_id)
    return render_template('places-inside-page.html', location=location)
