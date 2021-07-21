"""
Services are used to process business rules. It is commonly used to communcate
the router and the respository
"""
from flask import session
from project.enums import session_enum
from project.enums.session_enum import USER_ID


def is_authenticated():
    """
    Return true if the user is authenticated in the application
    """
    return USER_ID in session and len(session[USER_ID]) > 0


def do_login(email, password):
    """
    Authenticate user to application
    """
    if password != 'admin':
        return False
    session[session_enum.USER_ID] = email
    return True
