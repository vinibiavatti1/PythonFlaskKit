from flask import Blueprint
from typing import Any
from app import constants


processors = Blueprint('processors', __name__)


@processors.app_context_processor
def inject_config() -> dict[str, Any]:
    return dict(
        constants=constants
    )
