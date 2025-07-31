from app.config import config
from app.errors import AppError
from typing import Union, Any
import mysql.connector


def connect() -> object:
    """
    Connect to MySQL database and return the connection object.
    The connection data will be get from app configuration.
    """
    connection = mysql.connector.connect(
        host=config['db_host'],
        user=config['db_user'],
        password=config['db_pass'],
        port=config['db_port'],
        database=config['db_name']
    )
    if not connection:
        raise AppError('Could not connect to database')
    return connection


def execute_query(sql: str, values: tuple = (), *,
                  first_or_none: bool = False) -> Union[list, dict]:
    """
    Execute a SQL query and fetch the returned data.
    """
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, values)
    result_set = cursor.fetchall()
    if first_or_none:
        if len(result_set):
            return result_set[0]
        return None
    return result_set


def execute_paginated_query(sql: str, page: int, page_size: int,
                            values: tuple = ()) -> list:
    """
    Execute a statement adding the LIMIT control by page and page_size. The
    return will be a dict containing the fetch data and pagination properties.
    """
    sql_check = sql + f' LIMIT {page + 1},{page_size}'
    result_set = execute_query(sql_check, values)
    is_last = len(result_set) == 0
    sql += f' LIMIT {page},{page_size}'
    result_set = execute_query(sql, values)
    return dict(
        data=result_set,
        is_last=is_last,
        page=page,
        page_size=page_size
    )


def execute(sql: str, values: tuple = ()) -> None:
    """
    Execute a transactional statement into database.
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()


def count_table(table_name: str) -> int:
    """
    Return the record amount of table. If table was not found, None will be
    returned.
    """
    result_set = execute_query(
        f'SELECT COUNT(*) AS amount FROM `{table_name}`'
    )
    if len(result_set) > 0:
        return result_set[0]['amount']
    return None


def record_exists(table_name: str, id: int, field: str = 'id') -> bool:
    """
    Return True if the record with identifier was found in table, otherwise
    False.
    """
    result_set = execute_query(
        f'SELECT `{field}` FROM `{table_name}` WHERE id = %s',
        (id,)
    )
    return len(result_set) > 0


def last_inserted_record(table_name: str, order_column: str = 'id') -> dict:
    """
    Return the last inserted record by column ordering. If the table is empty
    or not find, None will be returned.
    """
    result_set = execute_query(
        f'SELECT * FROM `{table_name}` ORDER BY `{order_column}` DESC LIMIT 1'
    )
    if len(result_set) > 0:
        return result_set[0]
    return None


def last_inserted_id(table_name: str, id_column: str = 'id') -> Any:
    """
    Return the last inserted identifier by id column ordering. If the table is
    empty or not find, None will be returned.
    """
    result_set = execute_query(
        f'SELECT `{id_column}` AS id FROM `{table_name}` ORDER BY \
        `{id_column}` DESC LIMIT 1'
    )
    if len(result_set):
        return result_set[0]['id']
    return None


def describe_table(table_name: str) -> dict:
    """
    Describe table and return the table data.
    """
    result_set = execute_query(f'DESC `{table_name}`')
    if len(result_set):
        return result_set[0]
    return None


def is_record_from_user(table_name: str, user_id: int, record_id: int, *,
                        user_id_column: str = 'user_id',
                        id_column: str = 'id') -> bool:
    """
    Return True if the user is owner of the record, otherwise False.
    """
    sql = f'SELECT {id_column} FROM `{table_name}` \
        WHERE `{user_id_column}` = %s AND `{id_column}` = %s'
    result_set = execute_query(sql, (user_id, record_id))
    return len(result_set) > 0
