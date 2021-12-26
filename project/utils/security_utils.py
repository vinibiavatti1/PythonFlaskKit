from flask import abort, request, redirect
from functools import wraps
from project.utils.translation_utils import t
from flask.helpers import flash
from project.enums import session_enum
from flask import session
from typing import Callable
from hashlib import sha256
from project.config import config
from project.services.user_service import is_user_active
from project.services.auth_service import do_logout


###############################################################################
# Decorators
###############################################################################


def login_required(*, methods: tuple[str] = (),
                   permissions: tuple[int] = ()) -> Callable:
    """
    Validate user session before process the resource. Can be used to decorate
    route functions to set the route only if the user is authenticated. Set
    methods to block specific methods, otherwise, all methods will be blocked.
    """
    def decorator_wrapper(fn: Callable):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if methods and request.method not in methods:
                return fn(*args, **kwargs)
            if not is_authenticated():
                return abort(401)
            if permissions and not has_permission(permissions):
                return abort(401)
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


def validate_user_in_db() -> Callable:
    """
    Validates the user in database checking if user is active and not deleted.
    """
    def decorator_wrapper(fn: Callable):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not is_user_active(session[session_enum.USER_ID]):
                do_logout()
                flash(t('errors.session_expired'), category='error')
                return redirect('/login')
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


###############################################################################
# Functions
###############################################################################


def is_authenticated() -> bool:
    """
    Return true if the user is authenticated in the application
    """
    return (session_enum.USER_ID in session and
            len(str(session[session_enum.USER_ID])) > 0)


def has_permission(*permissions: int) -> bool:
    """
    Check if authenticated user has permission
    """
    user_permission = session.get(session_enum.USER_PERMISSION, None)
    if not user_permission:
        return False
    return user_permission in permissions


def generate_hash(data: tuple[str]) -> str:
    """
    Generate hash by data using config salt and SHA256
    """
    result = ''.join(data)
    result += config['salt']
    return sha256(result.encode()).hexdigest()
