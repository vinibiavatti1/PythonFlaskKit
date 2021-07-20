from project.errors.validation_error import ValidationError
from flask import Blueprint, request, render_template, flash
from markupsafe import escape
from project.validators import user_validator


# Blueprint
blueprint = Blueprint('user', __name__, url_prefix='/user')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/login', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('/user/login.html')
    try:
        user_validator.validate_user_login(request.form)
    except ValidationError as err:
        flash(err, category='error')
        return render_template('/user/login.html')
    email = escape(request.form.get('email'))
    password = request.form.get('password')
    # Do login and set data to session ...
    return render_template('/user/login.html')
