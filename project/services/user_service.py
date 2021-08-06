from project.utils import database_utils


def is_user_active(user_id: int) -> bool:
    """
    Return True if the user is active and not deleted, otherwise False.
    """
    sql = '''SELECT `id` FROM users WHERE `id` = %s AND `active` = 1
    AND `deleted` = 0'''
    result = database_utils.execute_query(sql, (user_id,), first_or_none=True)
    return result is not None
