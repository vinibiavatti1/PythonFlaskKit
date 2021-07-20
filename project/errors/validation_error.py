"""
Validation Error can be used by validators or services to validate form data
"""
from project.errors.app_error import AppError


class ValidationError(AppError):
    pass
