from flask import session, abort
from app.enums.role_enum import RoleEnum
from typing import Callable, Any
from app.repositories import user_repository
from functools import wraps


def login_required(roles: list[RoleEnum]) -> Callable:
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            user_id = session['user_id']
            user = user_repository.get_user(user_id) if user_id else None
            if not user or not user.active:
                return abort(401)
            role = RoleEnum(user.role)
            if role not in roles:
                return abort(403)
            return fn(*args, **kwargs)
        return wrapper
    return decorator
