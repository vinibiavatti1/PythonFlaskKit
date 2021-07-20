from flask import Blueprint, request, redirect, make_response


# Blueprint
blueprint = Blueprint('locale', __name__, url_prefix='/locale')


# Routes
@blueprint.route('/<lang>')
def register(lang):
    response = make_response(redirect(request.referrer))
    response.set_cookie('lang', lang)
    return response
