from app.errors import TranslationError
from app.i18n import translations_dict
from flask import request
from typing import Union


def get_translations(locale: str = None) -> dict:
    """
    Get the translations by the specified locale. If locale is None,
    the cookies will be check to find the user locale. If no locale found, the
    default locale will be considered
    """
    if locale is None:
        locale = request.cookies.get('locale', 'default')
    translations = translations_dict.get(locale, None)
    return translations


def get_locales() -> dict:
    """
    Get a dict of locales with code and name. The default locale will no be
    consider
    """
    locales = {}
    for code, data in translations_dict.items():
        if code == 'default':
            continue
        locales[code] = data['name']
    return locales


def translate(key: Union[tuple, str], locale: str = None) -> str:
    """
    Get value from translations by locale. If key is string, it will be
    splitted by dot "." to create a tuple. The key tuple will be used to find
    the sentence in the translations
    """
    translations = get_translations(locale)
    if isinstance(key, str):
        key = tuple(key.split('.'))
    for k in key:
        translations = translations.get(k, None)
        if translations is None:
            raise TranslationError(
                f'Key "{str(key)}" not found in dictionary of locale '
                f'"{locale}"'
            )
    sentence = translations
    if isinstance(sentence, dict):
        raise TranslationError(
            f'Invalid key "{str(key)}"'
        )
    return sentence


def t(key: Union[tuple, str], locale: str = None) -> str:
    """
    Alias to translate(key, locale)
    """
    return translate(key, locale)
