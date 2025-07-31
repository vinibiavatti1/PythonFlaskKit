from flask import Flask
from app.processors import processors
from app.handlers import handlers
from app.controllers.home_ctrl import home_ctrl
from app.controllers.config_ctrl import config_ctrl
from app.controllers.auth_ctrl import auth_ctrl
from app.controllers.public import (
    cookie_policy_ctrl,
)
from app.controllers.admin import (
    map_ctrl,
    chart_ctrl,
    list_ctrl,
    form_ctrl,
    calendar_ctrl,
)


blueprints = [
    processors,
    handlers,
    config_ctrl,
    home_ctrl,
    auth_ctrl,


    map_ctrl.blueprint,
    chart_ctrl.blueprint,
    list_ctrl.blueprint,
    form_ctrl.blueprint,
    cookie_policy_ctrl.blueprint,
    calendar_ctrl.blueprint,
    search_ctrl.blueprint,
]
