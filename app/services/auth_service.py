from flask import session
from app.repositories import user_repository
from app.filters.user_filter import UserFilter


def login(email: str, password_hash: str) -> bool:
    users = user_repository.list_users(
        UserFilter(email=email, password_hash=password_hash)
    )
    if len(users) == 1:
        user = users[0]
        session['user_id'] = user.id
        session['user_name'] = user.name
        session['user_email'] = user.email
        return True
    return False


def logout() -> None:
    session.clear()
