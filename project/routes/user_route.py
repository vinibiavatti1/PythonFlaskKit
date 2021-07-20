from flask import Blueprint, request, render_template
from markupsafe import escape


# Blueprint
blueprint = Blueprint('user', __name__, url_prefix='/user')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/login', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('/user/login.html')
    email = escape(request.form.get('email'))
    password = request.form.get('password')
    return render_template('/user/login.html')
