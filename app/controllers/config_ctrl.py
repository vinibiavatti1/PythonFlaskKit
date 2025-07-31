from flask import Blueprint, send_from_directory, current_app, request


config_ctrl = Blueprint('config_ctrl', __name__)


@config_ctrl.route('/robots.txt')
def robots():
    return send_from_directory(current_app.static_folder,
        'configs/robots.txt',
    )


@config_ctrl.route('/sitemap.xml')
def sitemap():
    return send_from_directory(current_app.static_folder,
        'configs/sitemap.txt',
    )


@config_ctrl.route('/ads.txt')
def ads():
    return send_from_directory(current_app.static_folder,
        'configs/ads.txt',
    )
