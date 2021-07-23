from flask import Blueprint, render_template
from project.utils.security_utils import login_required


# Blueprint
blueprint = Blueprint('map', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index():
    return render_template(
        '/backoffice/map.html',
        points=[(38.73, -9.14)],
        lat=38.73,
        lng=-9.14,
        zoom=12
    )
