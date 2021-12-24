from flask import session
from project.enums import session_enum, permission_enum
from project.utils.string_utils import get_name_abbreviation


def do_login(email: str, password: str) -> bool:
    """
    Authenticate user to application
    """
    if email != 'admin@admin.com' or password != 'admin':
        return False
    session[session_enum.USER_ID] = 1
    session[session_enum.USER_NAME] = 'admin'
    session[session_enum.USER_EMAIL] = email
    session[session_enum.USER_PERMISSION] = permission_enum.ADMIN
    session[session_enum.USER_ABBREVIATION] = get_name_abbreviation('admin')
    return True


def do_logout() -> None:
    """
    Destroy user session
    """
    session.clear()
