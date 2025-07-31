from flask import Blueprint, render_template
from app.utils.security_utils import login_required


# Blueprint
blueprint = Blueprint('form', __name__, url_prefix='/admin/form')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    return render_template('/admin/form.html', data={})
