from flask import Blueprint, request, redirect, make_response
from project.enums.cookie_enum import LOCALE


# Blueprint
blueprint = Blueprint('locale', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/<locale>')
def register(locale):
    response = make_response(redirect(request.referrer))
    response.set_cookie(LOCALE, locale)
    return response
