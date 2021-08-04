from typing import Union
from project.utils.translation_utils import t


###############################################################################
# Menus Build Functions
###############################################################################


def build_public_menu() -> list[Union[tuple, str]]:
    """
    Return a list with menus for public area
    """
    return [
        t('menus.titles.menu'),
        (t('menus.homepage'), '/', 'mdi-home'),
        (t('menus.login'), '/login', 'mdi-login-variant'),
    ]


def build_private_menu() -> list[Union[tuple, str]]:
    """
    Return a list with menus for member area
    """
    return []


def build_admin_manu() -> list[Union[tuple, str]]:
    """
    Return a list with menus for admin area
    """
    return [
        t('menus.titles.menu'),
        (t('menus.homepage'), '/', 'mdi-home'),
        (t('menus.map'), '/admin/map', 'mdi-map'),
        (t('menus.chart'), '/admin/chart', 'mdi-chart-box'),
        (t('menus.list'), '/admin/list', 'mdi-table-large'),
        (t('menus.form'), '/admin/form', 'mdi-auto-fix'),
        t('menus.titles.user'),
        (t('menus.logout'), '/logout', 'mdi-logout-variant'),
    ]
