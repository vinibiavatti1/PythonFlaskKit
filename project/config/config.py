import os
from project.config.config_dev import config as dev
from project.config.config_prod import config as prod
from project.config.config_test import config as test


# Set config by FLASK_ENV variable
config = None
env = os.environ.get('FLASK_ENV')
if env == 'testing':
    config = test
elif env == 'production':
    config = prod
else:
    config = dev
