from flask import Blueprint, render_template


# Blueprint
blueprint = Blueprint('handlers', __name__)


###############################################################################
# Error handlers
###############################################################################


@blueprint.app_errorhandler(400)
def bad_request(error_message):
    """
    Bad request (400) error handler
    """
    return render_template('errors/400.html', error_message=error_message), 404


@blueprint.app_errorhandler(401)
def unauthorized(error_message):
    """
    Unauthorized (401) error handler
    """
    return render_template('errors/401.html', error_message=error_message), 401


@blueprint.app_errorhandler(403)
def forbidden(error_message):
    """
    Forbidden (403) error handler
    """
    return render_template('errors/403.html', error_message=error_message), 403


@blueprint.app_errorhandler(404)
def not_found(error_message):
    """
    Not found (404) error handler
    """
    return render_template('errors/404.html', error_message=error_message), 404


@blueprint.app_errorhandler(500)
def internal_server_error(error_message):
    """
    Internal server error (500) error handler
    """
    return render_template('errors/500.html', error_message=error_message), 500
