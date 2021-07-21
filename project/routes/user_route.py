from werkzeug.utils import redirect
from project.errors.errors import ValidationError
from flask import Blueprint, request, render_template, flash
from markupsafe import escape
from project.validators import user_validator
from project.services import user_service


# Blueprint
blueprint = Blueprint('user', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/login', methods=['GET'])
def login():
    return render_template('/user/login.html')


@blueprint.route('/login', methods=['POST'])
def login_action():
    # Validate form data
    try:
        user_validator.validate_user_login(request.form)
    except ValidationError as err:
        flash(err, category='error')
        return render_template('/user/login.html')

    # Do login
    email = escape(request.form.get('email'))
    password = request.form.get('password')
    if user_service.do_login(email, password):
        return redirect('/')
    flash('Invalid user and/or password', category='error')
    return render_template('/user/login.html')
