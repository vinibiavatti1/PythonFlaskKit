from flask import Blueprint, session
from typing import Any
from app import constants


processors = Blueprint('processors', __name__)


@processors.app_context_processor
def inject() -> dict[str, Any]:
    return dict(
        constants=constants,
        session=session
    )
