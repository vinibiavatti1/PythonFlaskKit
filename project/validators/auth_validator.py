from project.errors import ValidationError
from project.utils.translation_utils import t


def validate_login_data(form_data: dict) -> None:
    """
    Validate form data for login route (example). Raises ValidationError if
    the validation failed.
    """
    if 'email' not in form_data:
        raise ValidationError(
            t('feedbacks.required').format('email')
        )
    elif 'password' not in form_data:
        raise ValidationError(
            t('feedbacks.required').format('password')
        )
