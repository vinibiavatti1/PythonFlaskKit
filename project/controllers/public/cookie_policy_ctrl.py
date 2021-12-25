from flask import Blueprint, request, make_response, redirect
from project.enums.cookie_enum import CookieEnum


# Blueprint
blueprint = Blueprint('cookie_policy', __name__, url_prefix='/cookie-policy')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/agree')
def agree():
    response = make_response(redirect(request.referrer))
    response.set_cookie(CookieEnum.COOKIE_POLICY.value, '1')
    return response


@blueprint.route('/disagree')
def disagree():
    response = make_response(redirect(request.referrer))
    response.set_cookie(CookieEnum.COOKIE_POLICY.value, '0')
    return response
