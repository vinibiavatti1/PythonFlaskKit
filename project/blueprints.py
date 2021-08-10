from flask import Flask
from project.processors import blueprint as processors
from project.handlers import blueprint as handlers
from project.controllers.public import (
    auth_ctrl,
    homepage_ctrl,
    locale_ctrl,
    cookie_policy_ctrl
)
from project.controllers.admin import (
    map_ctrl,
    chart_ctrl,
    list_ctrl,
    form_ctrl,
)


def register_blueprints(app: Flask) -> None:
    """
    Register blueprints of project into flask application.
    """
    app.register_blueprint(
        processors
    )
    app.register_blueprint(
        handlers
    )
    app.register_blueprint(
        homepage_ctrl.blueprint
    )
    app.register_blueprint(
        auth_ctrl.blueprint
    )
    app.register_blueprint(
        locale_ctrl.blueprint, url_prefix='/locale'
    )
    app.register_blueprint(
        map_ctrl.blueprint, url_prefix='/admin/map'
    )
    app.register_blueprint(
        chart_ctrl.blueprint, url_prefix='/admin/chart'
    )
    app.register_blueprint(
        list_ctrl.blueprint, url_prefix='/admin/list'
    )
    app.register_blueprint(
        form_ctrl.blueprint, url_prefix='/admin/form'
    )
    app.register_blueprint(
        cookie_policy_ctrl.blueprint, url_prefix='/cookie-policy'
    )
