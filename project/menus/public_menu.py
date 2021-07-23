from project.models.menu_models import Menu, MenuOptions
from project.utils.translation_utils import translate
from project.services.auth_service import is_authenticated


class PublicMenu(Menu):

    def rule(self) -> bool:
        return not is_authenticated()

    def build(self) -> MenuOptions:
        return MenuOptions() \
            .with_option(
                translate('menus.homepage'),
                '/',
                'mdi-home'
            ) \
            .with_option(
                translate('menus.login'),
                '/login',
                'mdi-login-variant'
            )
