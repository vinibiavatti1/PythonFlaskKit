from werkzeug.utils import redirect
from project.errors import ValidationError
from flask import Blueprint, request, render_template, flash
from markupsafe import escape
from project.validators import auth_validator
from project.services import auth_service


# Blueprint
blueprint = Blueprint('auth', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/login', methods=['GET'])
def login():
    return render_template('/auth/login.html')


@blueprint.route('/login', methods=['POST'])
def login_action():
    # Validate form data
    try:
        auth_validator.validate_login_data(request.form)
    except ValidationError as err:
        flash(err, category='error')
        return render_template('/auth/login.html')

    # Do login
    email = escape(request.form.get('email'))
    password = request.form.get('password')
    if auth_service.do_login(email, password):
        return redirect('/')
    flash('Invalid user and/or password', category='error')
    return render_template('/auth/login.html')


@blueprint.route('/logout')
def logout():
    auth_service.do_logout()
    return render_template('/home/homepage.html')
