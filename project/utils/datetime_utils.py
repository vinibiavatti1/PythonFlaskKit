from typing import Union, Any
from datetime import date, datetime
from project.config import config


###############################################################################
# Constants
###############################################################################


HTML_DATE_FORMAT = '%Y-%m-%d'
HTML_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'
CONFIG_DATE_FORMAT = config['date_format']
CONFIG_DATETIME_FORMAT = config['datetime_format']


###############################################################################
# Functions
###############################################################################


def format_date_to_str(date: Union[date, datetime], format: str) -> str:
    """
    Format date or datetime to string by given format. Use module constants to
    specific formats.
    """
    return date.strftime(format)


def format_list_dates_to_str(lst: list[Any], format: str) -> str:
    """
    Format all dates or datetimes inside the list to string by given format.
    """
    for item in lst:
        if isinstance(item, (date, datetime)):
            item = format_date_to_str(item, format)
    return lst


def format_dict_dates_to_str(dct: dict[Any], format: str) -> str:
    """
    Format all dates and datetimes inside the dict to string by given format.
    """
    for key, val in dct.items():
        if isinstance(val, (date, datetime)):
            dct[key] = format_date_to_str(val, format)
    return dct
