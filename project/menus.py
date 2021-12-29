from typing import Union
from project.utils.translation_utils import t


###############################################################################
# Menus Build Functions
###############################################################################


def build_public_menu() -> list[Union[tuple, str]]:
    """
    Return a list with menus for public area
    """
    return {
        t('menus.titles.menu'): [
            (t('menus.homepage'), '/', 'bi-house'),
            (t('menus.login'), '/login', 'bi-box-arrow-in-right'),
        ]
    }


def build_private_menu() -> list[Union[tuple, str]]:
    """
    Return a list with menus for member area
    """
    return []


def build_admin_manu() -> list[Union[tuple, str]]:
    """
    Return a list with menus for admin area
    """
    return {
        t('menus.titles.menu'): [
            (t('menus.homepage'), '/', 'bi-house'),
            (t('menus.map'), '/admin/map', 'bi-map'),
            (t('menus.chart'), '/admin/chart', 'bi-bar-chart'),
            (t('menus.list'), '/admin/list', 'bi-table'),
            (t('menus.form'), '/admin/form', 'bi-ui-checks'),
            (t('menus.calendar'), '/admin/calendar', 'bi-calendar-date'),
        ],
        t('menus.titles.user'): [
            (t('menus.logout'), '/logout', 'bi-box-arrow-in-right'),
        ]
    }
