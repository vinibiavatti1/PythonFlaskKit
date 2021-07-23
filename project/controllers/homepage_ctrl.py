from flask import Blueprint, render_template


# Blueprint
blueprint = Blueprint('homepage', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
def index():
    return render_template('/homepage/index.html')
