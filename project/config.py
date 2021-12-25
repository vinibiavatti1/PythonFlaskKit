import os
from project.enums.env_enum import EnvEnum
from project.configs.config_dev import config as dev_config
from project.configs.config_prod import config as prod_config
from project.configs.config_test import config as test_config


# Set config by FLASK_ENV variable
config = None
env = os.environ.get('FLASK_ENV')
if env == EnvEnum.TESTING.value:
    config = test_config
elif env == EnvEnum.PRODUCTION.value:
    config = prod_config
else:
    config = dev_config
