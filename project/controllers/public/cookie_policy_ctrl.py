from flask import Blueprint, request, make_response, redirect
from project.enums.cookie_enum import COOKIE_POLICY


# Blueprint
blueprint = Blueprint('cookie_policy', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/agree')
def agree():
    response = make_response(redirect(request.referrer))
    response.set_cookie(COOKIE_POLICY, '1')
    return response


@blueprint.route('/disagree')
def disagree():
    response = make_response(redirect(request.referrer))
    response.set_cookie(COOKIE_POLICY, '0')
    return response
