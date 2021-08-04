from werkzeug import utils
from typing import Any


def escape_dict(data: dict) -> dict:
    """
    Escape all fields of dict
    """
    return {k: utils.escape(v) for k, v in data.items()}


def escape(value: Any) -> str:
    """
    Alias to werkzeug.utils.escape()
    """
    return utils.escape(value)
