from flask import Flask
from project.processors import blueprint as processors
from project.handlers import blueprint as handlers
from project.controllers.public import (
    seo_ctrl,
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
    calendar_ctrl,
)


# Blueprints
blueprints = [
    processors,
    handlers,
    seo_ctrl.blueprint,
    homepage_ctrl.blueprint,
    auth_ctrl.blueprint,
    locale_ctrl.blueprint,
    map_ctrl.blueprint,
    chart_ctrl.blueprint,
    list_ctrl.blueprint,
    form_ctrl.blueprint,
    cookie_policy_ctrl.blueprint,
    calendar_ctrl.blueprint,
]


###############################################################################
# Functions
###############################################################################


def register_blueprints(app: Flask) -> None:
    """
    Register blueprints into flask application.
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
