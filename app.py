from flask import Flask
from project.config.config import config
from project.processors.context_processor import blueprint as context_processor
from project.handlers.error_handlers import blueprint as error_handlers
from project.routes.user_route import blueprint as user_route
from project.routes.homepage_route import blueprint as homepage_route
from project.routes.locale_route import blueprint as locale_route
from project.routes.backoffice.map_route import blueprint as map_route

###############################################################################
# Init flask
###############################################################################


# Init flask and set the secret key
app = Flask(__name__)
app.secret_key = config['secret_key']


###############################################################################
# Register blueprints
###############################################################################


# Processors
app.register_blueprint(context_processor)

# Handlers
app.register_blueprint(error_handlers)

# Routes
app.register_blueprint(homepage_route)
app.register_blueprint(user_route, url_prefix='/user')
app.register_blueprint(locale_route, url_prefix='/locale')

# Backoffice
app.register_blueprint(map_route, url_prefix='/backoffice/map')
