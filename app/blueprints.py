from app.processors import processors
from app.handlers import handlers
from app.controllers.home_ctrl import home_ctrl
from app.controllers.config_ctrl import config_ctrl
from app.controllers.auth_ctrl import auth_ctrl
from app.controllers.chart_ctrl import chart_ctrl
from app.controllers.map_ctrl import map_ctrl
from app.controllers.calendar_ctrl import calendar_ctrl
from app.controllers.datatable_ctrl import datatable_ctrl
from app.controllers.register_ctrl import register_ctrl


blueprints = [
    processors,
    handlers,
    config_ctrl,
    home_ctrl,
    auth_ctrl,
    chart_ctrl,
    map_ctrl,
    calendar_ctrl,
    datatable_ctrl,
    register_ctrl,
]
