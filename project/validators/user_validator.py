"""
Validators can be used to define validations for the route POST data
"""
from project.errors.validation_error import ValidationError


def validate_user_login(form_data):
    """
    Validate form data for login route (example)
    """
    if 'login' not in form_data:
        raise ValidationError('login not defined')
    elif 'password' not in form_data:
        raise ValidationError('password not defined')
