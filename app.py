from flask import Flask
from project.config.config import config
from project.processors import blueprint as processors
from project.handlers import blueprint as handlers
from project.controllers import (
    auth_ctrl,
    homepage_ctrl,
    locale_ctrl,
)
from project.controllers.backoffice import (
    map_ctrl,
    chart_ctrl,
    datatable_ctrl,
    crud_ctrl
)


###############################################################################
# Init flask
###############################################################################


# Init flask and set the secret key
app = Flask(__name__)
app.secret_key = config['secret_key']


###############################################################################
# Register blueprints
###############################################################################


# Register configuration
app.register_blueprint(processors)
app.register_blueprint(handlers)

# Register controllers
app.register_blueprint(homepage_ctrl.blueprint)
app.register_blueprint(auth_ctrl.blueprint)
app.register_blueprint(locale_ctrl.blueprint,
                       url_prefix='/locale')
app.register_blueprint(map_ctrl.blueprint,
                       url_prefix='/backoffice/map')
app.register_blueprint(chart_ctrl.blueprint,
                       url_prefix='/backoffice/chart')
app.register_blueprint(datatable_ctrl.blueprint,
                       url_prefix='/backoffice/datatable')
app.register_blueprint(crud_ctrl.blueprint,
                       url_prefix='/backoffice/crud')
