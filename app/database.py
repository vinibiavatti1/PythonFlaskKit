import mysql.connector
from mysql.connector import MySQLConnection
from app.errors.app_error import AppError
from app.env import get_env


def connect() -> MySQLConnection:
    env = get_env()
    connection = mysql.connector.connect(
        host=env['db_host'],
        user=env['db_user'],
        password=env['db_pass'],
        port=env['db_port'],
        database=env['db_name']
    )
    if not connection:
        raise AppError('Could not connect to database')
    return connection
