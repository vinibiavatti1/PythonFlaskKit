from flask import Flask
from app.processors import processors
from app.handlers import handlers
from app.controllers.home_ctrl import home_ctrl
from app.controllers.config_ctrl import config_ctrl
from app.controllers.auth_ctrl import auth_ctrl

blueprints = [
    processors,
    handlers,
    config_ctrl,
    home_ctrl,
    auth_ctrl,
]
