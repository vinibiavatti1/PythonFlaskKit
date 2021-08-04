from flask import Blueprint, request, redirect, make_response


# Blueprint
blueprint = Blueprint('locale', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/<locale>')
def register(locale):
    response = make_response(redirect(request.referrer))
    response.set_cookie('locale', locale)
    return response
