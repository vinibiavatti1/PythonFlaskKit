from flask import Blueprint, render_template
from project.decorators import auth


# Blueprint
blueprint = Blueprint('map', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@auth.login_required()
def index():
    return render_template('/backoffice/map.html')
