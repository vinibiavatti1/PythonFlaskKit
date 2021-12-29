from project.errors import ValidationError
from project.utils.translation_utils import t
from project.config import config
import requests


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


def validate_recaptcha(token: str) -> None:
    """
    Validate the score of the ReCaptcha token. ReCaptcha v3 returns a score
    (1.0 is very likely a good interaction, 0.0 is very likely a bot).
    """
    response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': config['recaptcha_secret_key'],
            'response': token,
        }
    )
    message = 'Invalid ReCaptcha. Please, try again.'
    if response.status_code != 200:
        raise ValidationError(message)
    json = response.json()
    if not json['success']:
        raise ValidationError(message)
    if json['score'] <= config['recaptcha_threshold']:
        raise ValidationError(message)
