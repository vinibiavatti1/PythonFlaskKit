from flask import Blueprint
from typing import Any
from app import env
from app.props import props


processors = Blueprint('processors', __name__)


@processors.app_context_processor
def inject_config() -> dict[str, Any]:
    return dict(
        env=env.get_env(),
        props=props
    )
