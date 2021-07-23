from project.errors import TranslationError
from project.dictionaries.registry import dictionaries
from flask import request
from typing import Union


def get_dictionary(locale: str = None) -> dict:
    """
    Get the dictionary by the specified locale. If locale is None, the cookies
    will be check to find the user locale. If no locale found, the default
    locale will be used
    """
    if locale is None:
        locale = request.cookies.get('locale', 'default')
    dictionary = dictionaries.get(locale, None)
    return dictionary


def translate(key: Union[tuple, str], locale: str = None) -> str:
    """
    Get value from dictionary by locale. If key is string, it will be splitted
    by dot "." to create a tuple. The key tuple will be used to find the
    sentence in the dictionary
    """
    dictionary = get_dictionary(locale)
    if isinstance(key, str):
        key = tuple(key.split('.'))
    for k in key:
        dictionary = dictionary.get(k, None)
        if dictionary is None:
            raise TranslationError(
                f'Key "{str(key)}" not found in dictionary of locale '
                f'"{locale}"'
            )
    sentence = dictionary
    if isinstance(sentence, dict):
        raise TranslationError(
            f'Invalid key "{str(key)}"'
        )
    return sentence
