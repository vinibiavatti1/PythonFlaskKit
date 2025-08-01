from flask import Blueprint
from typing import Any
from app import props


processors = Blueprint('processors', __name__)


@processors.app_context_processor
def inject_config() -> dict[str, Any]:
    return dict(
        props=props
    )
