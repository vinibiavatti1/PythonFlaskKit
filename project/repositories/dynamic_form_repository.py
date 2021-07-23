from project.utils import database_utils


def find_by_id(table_name, id, form_fields):
    """
    Find record by id dinamically
    """
    fields = ''
    comma = ''
    for field in form_fields:
        fields += comma + f'`{field}`'
        comma = ', '
    sql = f'SELECT {fields} FROM `{table_name}` WHERE `id` = %s'
    result = database_utils.execute_query(sql, (id,))
    return database_utils.format_date_fields_to_html_format(result)


def insert(table_name, dict_data):
    """
    Insert to database table dinamically
    """
    fields = ''
    targets = ''
    values = []
    comma = ''
    for key, val in dict_data.items():
        fields += comma + f'`{str(key)}`'
        targets += comma + '%s'
        comma = ', '
        values.append(val)
    sql = f'INSERT INTO `{table_name}` ({fields}) VALUES ({targets})'
    print(sql)
    database_utils.execute(sql, values)


def update(table_name, id, dict_data):
    print(table_name, id, dict_data)
    """
    Update record in database table dinamically
    """
    fields = ''
    values = []
    comma = ''
    for key, val in dict_data.items():
        fields += comma + f'`{str(key)}` = %s'
        comma = ', '
        values.append(val)
    values.append(id)
    sql = f'UPDATE `{table_name}` SET {fields} WHERE `id` = %s'
    print(sql)
    database_utils.execute(sql, values)
