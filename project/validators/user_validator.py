"""
Validators can be used to define validations for the route POST data
"""
from project.errors.errors import ValidationError


def validate_user_login(form_data):
    """
    Validate form data for login route (example)
    """
    if 'email' not in form_data:
        raise ValidationError('email not defined')
    elif 'password' not in form_data:
        raise ValidationError('password not defined')
