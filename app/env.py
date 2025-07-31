from flask import g
from typing import Any
from app.errors.app_error import AppError
from app.enums.env_enum import EnvEnum
from app.envs.env_dev import env_dev
from app.envs.env_prod import env_prod


def get_env() -> dict[str, Any]:
    if g.env == EnvEnum.DEV:
        return env_dev
    elif g.env == EnvEnum.PROD:
        return env_prod
    else:
        raise AppError(f'Invalid env: {g.env}')
