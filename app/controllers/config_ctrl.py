from flask import Blueprint, send_from_directory, current_app, Response


config_ctrl = Blueprint('config_ctrl', __name__)


@config_ctrl.route('/robots.txt')
def robots() -> Response:
    return send_from_directory(
        str(current_app.static_folder),
        'configs/robots.txt',
    )


@config_ctrl.route('/sitemap.xml')
def sitemap() -> Response:
    return send_from_directory(
        str(current_app.static_folder),
        'configs/sitemap.txt',
    )


@config_ctrl.route('/ads.txt')
def ads() -> Response:
    return send_from_directory(
        str(current_app.static_folder),
        'configs/ads.txt',
    )
