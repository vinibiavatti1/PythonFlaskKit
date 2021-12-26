from flask import Blueprint, request, redirect, make_response
from project.enums import cookie_enum


# Blueprint
blueprint = Blueprint('locale', __name__, url_prefix='/locale')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/<locale>')
def register(locale):
    response = make_response(redirect(request.referrer))
    response.set_cookie(cookie_enum.LOCALE, locale)
    return response
