from werkzeug import utils
from typing import Any


def escape_dict(data: dict) -> dict:
    """
    Escape all fields of dict.
    """
    return {k: utils.escape(v) for k, v in data.items()}


def escape(value: Any) -> str:
    """
    Alias to werkzeug.utils.escape().
    """
    return utils.escape(value)


def result_api_message(type: str, message: str) -> dict:
    """
    Generates a common dict response message with type and message.
    """
    return {
        'type': type,
        'message': message
    }
