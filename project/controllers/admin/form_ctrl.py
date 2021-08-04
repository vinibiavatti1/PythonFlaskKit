from flask import Blueprint, render_template
from project.utils.security_utils import login_required


# Blueprint
blueprint = Blueprint('form', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    return render_template('/admin/form.html', data={})
