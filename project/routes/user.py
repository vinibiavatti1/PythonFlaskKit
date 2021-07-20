from flask import Blueprint, request, render_template


# Blueprint
blueprint = Blueprint('user', __name__, url_prefix='/user')


# Routes
@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('/user/register.html')
    # TODO
