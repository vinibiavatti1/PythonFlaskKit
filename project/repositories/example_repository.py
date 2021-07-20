"""
Repositories are used to control the database directly
"""
from project.utils import database_util


def insert(name, email, password):
    """
    Insert a new user (example)
    """
    sql = ''''INSERT INTO user (name, email, password) VALUES (%s, %s, %s)'''
    database_util.execute(
        sql,
        (name, email, password)
    )


def find_all():
    """
    Select all users (example)
    """
    sql = ''''SELECT * FROM user'''
    return database_util.execute_query(
        sql
    )
