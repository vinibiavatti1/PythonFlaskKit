from datetime import datetime, date
from project.config.config import config
from project.errors import AppError
import mysql.connector


def connect():
    """
    Connect to MySQL database and return the connection object.
    The connection data will be get from app configuration
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


def execute_query(sql, values=()):
    """
    Execute a SQL query and fetch the returned data
    """
    connection = connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, values)
    return cursor.fetchall()


def execute_query_paginated(sql, page, page_size, values=()):
    """
    Execute a statement adding the LIMIT control by page and page_size. The
    return will be a dict containing the fetch data and pagination properties
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


def execute(sql, values=()):
    """
    Execute a transactional statement into database
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql, values)
    connection.commit()


def count_table(table_name):
    """
    Return the record amount of table. If table was not found, None will be
    returned
    """
    result_set = execute_query(
        f'SELECT COUNT(*) AS amount FROM `{table_name}`'
    )
    print(result_set)
    if len(result_set) > 0:
        return result_set[0]['amount']
    return None


def record_exists(table_name, id, field='id'):
    """
    Return True if the record with identifier was found in table, otherwise
    False
    """
    result_set = execute_query(
        f'SELECT `{field}` FROM `{table_name}` WHERE id = %s',
        (id,)
    )
    return len(result_set) > 0


def last_inserted_record(table_name, order_column='id'):
    """
    Return the last inserted record by column ordering. If the table is empty
    or not find, None will be returned
    """
    result_set = execute_query(
        f'SELECT * FROM `{table_name}` ORDER BY `{order_column}` DESC LIMIT 1'
    )
    if len(result_set) > 0:
        return result_set[0]
    return None


def last_inserted_id(table_name, id_column='id'):
    """
    Return the last inserted identifier by id column ordering. If the table is
    empty or not find, None will be returned
    """
    result_set = execute_query(
        f'SELECT `{id_column}` AS id FROM `{table_name}` ORDER BY ' +
        f'`{id_column}` DESC LIMIT 1'
    )
    if len(result_set) > 0:
        return result_set[0]['id']
    return None


def describe_table(table_name):
    """
    Describe table and return the table data
    """
    return execute_query(f'DESC `{table_name}`')


def format_date_fields(result_set, *, date_format, datetime_format):
    """
    Convert the database result set date and datetime to string
    """
    for record in result_set:
        for key, val in record.items():
            if isinstance(val, datetime):
                record[key] = val.strftime(datetime_format)
            elif isinstance(val, date):
                record[key] = val.strftime(date_format)
    return result_set


def format_date_fields_to_html_format(result_set):
    """
    Format result set date fields to HTML format (RFC 3339)
    """
    return format_date_fields(
        result_set,
        date_format='%Y-%m-%d',
        datetime_format='%Y-%m-%dT%H:%M'
    )


def format_date_fields_to_config_format(result_set):
    """
    Format result set date fields to the format defined in app configuration
    """
    return format_date_fields(
        result_set,
        date_format=config['date_format'],
        datetime_format=config['datetime_format']
    )
