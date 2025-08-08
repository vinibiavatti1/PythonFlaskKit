from flask import Blueprint, render_template


error_handlers = Blueprint('error_handlers', __name__)


@error_handlers.app_errorhandler(400)
def error_400(message: str) -> tuple[str, int]:
    return render_template(
        'pages/error.html',
        code=400,
        message=message
    ), 400


@error_handlers.app_errorhandler(401)
def error_401(message: str) -> tuple[str, int]:
    return render_template(
        'pages/error.html',
        code=401,
        message=message
    ), 401


@error_handlers.app_errorhandler(403)
def error_403(message: str) -> tuple[str, int]:
    return render_template(
        'pages/error.html',
        code=403,
        message=message
    ), 403


@error_handlers.app_errorhandler(404)
def error_404(message: str) -> tuple[str, int]:
    return render_template(
        'pages/error.html',
        code=404,
        message=message
    ), 404


@error_handlers.app_errorhandler(500)
def error_500(message: str) -> tuple[str, int]:
    return render_template(
        'pages/error.html',
        code=500,
        message=message
    ), 500
