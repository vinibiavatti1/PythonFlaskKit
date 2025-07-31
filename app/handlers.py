from flask import Blueprint, render_template


handlers = Blueprint('handlers', __name__)


@handlers.app_errorhandler(400)
def error_400():
    return render_template(
        'pages/error.html',
        code=400,
        message='Bad Request'
    ), 400


@handlers.app_errorhandler(401)
def error_401():
    return render_template(
        'pages/error.html',
        code=401,
        message='Unauthorized'
    ), 401


@handlers.app_errorhandler(403)
def error_403():
    return render_template(
        'pages/error.html',
        code=403,
        message='Forbidden'
    ), 403


@handlers.app_errorhandler(404)
def error_404():
    return render_template(
        'pages/error.html',
        code=404,
        message='Not Found'
    ), 404


@handlers.app_errorhandler(500)
def error_500():
    return render_template(
        'pages/error.html',
        code=500,
        message='Internal Server Error'
    ), 500
