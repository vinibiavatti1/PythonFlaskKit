from flask import session
from project.enums.session_enum import SessionEnum
from project.enums.permission_enum import PermissionEnum
from project.utils.string_utils import get_name_abbreviation


def do_login(email: str, password: str) -> bool:
    """
    Authenticate user to application
    """
    if email != 'admin@admin.com' or password != 'admin':
        return False
    session[SessionEnum.USER_ID.value] = 1
    session[SessionEnum.USER_NAME.value] = 'admin'
    session[SessionEnum.USER_EMAIL.value] = email
    session[SessionEnum.USER_PERMISSION.value] = PermissionEnum.ADMIN.value
    session[SessionEnum.USER_ABBREVIATION.value] = \
        get_name_abbreviation('admin')
    return True


def do_logout() -> None:
    """
    Destroy user session
    """
    session.clear()
