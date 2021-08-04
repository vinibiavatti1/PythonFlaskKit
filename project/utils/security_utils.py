from flask import abort, request
from functools import wraps
from project.enums.session_enum import USER_ID
from project.enums import session_enum
from flask import session
from typing import Callable


def login_required(*, methods: tuple[str] = [],
                   permissions: tuple[str] = []) -> Callable:
    """
    Validate user session before process the resource. Can be used to decorate
    route functions to set the route only if the user is authenticated. Set
    methods to block specific methods, otherwise, all methods will be blocked.
    """
    def decorator_wrapper(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if methods and request.method not in methods:
                return fn(*args, **kwargs)
            if is_authenticated():
                if len(permissions) and not has_permission(permissions):
                    return abort(401)
                return fn(*args, **kwargs)
            return abort(401)
        return wrapper
    return decorator_wrapper


def is_authenticated() -> bool:
    """
    Return true if the user is authenticated in the application
    """
    return USER_ID in session and len(session[USER_ID]) > 0


def has_permission(*permissions: int) -> bool:
    """
    Check if authenticated user has permission
    """
    user_permission = session.get(session_enum.USER_PERMISSION, None)
    if not user_permission:
        return False
    return user_permission in permissions
