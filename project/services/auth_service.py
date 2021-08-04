from flask import session
from project.enums import session_enum, permission_enum


def do_login(email: str, password: str) -> bool:
    """
    Authenticate user to application
    """
    if password != 'admin':
        return False
    session[session_enum.USER_ID] = email
    session[session_enum.USER_NAME] = 'admin'
    session[session_enum.USER_EMAIL] = email
    session[session_enum.USER_PERMISSION] = permission_enum.ADMIN
    return True


def do_logout() -> None:
    """
    Destroy user session
    """
    session.clear()
