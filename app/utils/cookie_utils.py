from flask import request
from app.enums import cookie_enum


def cookie_policy_consent() -> bool:
    """
    Return True if user accepted the cookie policy, False if not, or None if
    the user didn't answer anything.
    """
    answer = request.cookies.get(cookie_enum.COOKIE_POLICY, None)
    if answer is not None:
        return True if answer == '1' else False
    else:
        return None
