from flask import request
from project.enums.cookie_enum import COOKIE_POLICY


def cookie_policy_consent() -> bool:
    """
    Return True if user accepted the cookie policy, False if not, or None if
    the user didn't answer anything.
    """
    answer = request.cookies.get(COOKIE_POLICY, None)
    if answer is not None:
        return True if answer == '1' else False
    else:
        return None
