class AppError(Exception):
    """
    Base application error
    """
    pass


class ValidationError(AppError):
    """
    Application validation error
    """
    pass
