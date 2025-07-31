from flask import Blueprint, render_template
from app.utils.security_utils import login_required


# Blueprint
blueprint = Blueprint('map', __name__, url_prefix='/admin/map')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    return render_template(
        '/admin/map.html',
        points=[(38.73, -9.14)],
        lat=38.73,
        lng=-9.14,
        zoom=12
    )
