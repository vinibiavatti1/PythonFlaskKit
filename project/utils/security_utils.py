from flask import abort, request
from functools import wraps
from project.services.auth_service import is_authenticated


def login_required(methods: list = []):
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
                return fn(*args, **kwargs)
            abort(401)
        return wrapper
    return decorator_wrapper
