from flask import Blueprint, send_from_directory, current_app, request


# Blueprint
blueprint = Blueprint('seo', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/robots.txt')
@blueprint.route('/sitemap.xml')
def seo_files():
    return send_from_directory(
        current_app.static_folder,
        f'seo/{request.path[1:]}',
    )
