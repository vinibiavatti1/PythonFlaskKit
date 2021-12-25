from flask import Blueprint, request, redirect, make_response
from project.enums.cookie_enum import CookieEnum


# Blueprint
blueprint = Blueprint('locale', __name__, url_prefix='/locale')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/<locale>')
def register(locale):
    response = make_response(redirect(request.referrer))
    response.set_cookie(CookieEnum.LOCALE, locale)
    return response
