from flask import Blueprint, request, render_template


# Blueprint
blueprint = Blueprint('homepage', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
def index():
    return render_template('/home/homepage.html')
