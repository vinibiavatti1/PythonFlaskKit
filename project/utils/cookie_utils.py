from flask import request
from project.enums.cookie_enum import CookieEnum


def cookie_policy_consent() -> bool:
    """
    Return True if user accepted the cookie policy, False if not, or None if
    the user didn't answer anything.
    """
    answer = request.cookies.get(CookieEnum.COOKIE_POLICY.value, None)
    if answer is not None:
        return True if answer == '1' else False
    else:
        return None
