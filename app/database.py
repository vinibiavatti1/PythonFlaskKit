import mysql.connector
import os
from mysql.connector import MySQLConnection
from app.errors.app_error import AppError


def connect() -> MySQLConnection:
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
    )
    if not connection:
        raise AppError('Could not connect to database')
    return connection
