from project.errors import ValidationError


def validate_login_data(form_data):
    """
    Validate form data for login route (example)
    """
    if 'email' not in form_data:
        raise ValidationError('email not defined')
    elif 'password' not in form_data:
        raise ValidationError('password not defined')
