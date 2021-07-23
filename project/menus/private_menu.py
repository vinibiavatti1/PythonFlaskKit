from project.models.menu_models import Menu, MenuOptions
from project.utils.translation_utils import translate
from project.services.auth_service import is_authenticated


class PrivateMenu(Menu):

    def rule(self) -> bool:
        return is_authenticated()

    def build(self) -> MenuOptions:
        return MenuOptions() \
            .with_option(
                translate('menus.homepage'),
                '/',
                'mdi-home'
            ) \
            .with_option(
                translate('menus.map'),
                '/backoffice/map',
                'mdi-map'
            ) \
            .with_option(
                translate('menus.chart'),
                '/backoffice/chart',
                'mdi-chart-box'
            ) \
            .with_option(
                translate('menus.datatable'),
                '/backoffice/datatable',
                'mdi-table-large'
            ) \
            .with_option(
                translate('menus.crud'),
                '/backoffice/crud/example/form',
                'mdi-auto-fix'
            ) \
            .with_option(
                translate('menus.logout'),
                '/logout',
                'mdi-logout-variant'
            )
