from project.models.menu_models import Menu
from project.menus.private_menu import PrivateMenu
from project.menus.public_menu import PublicMenu


# Register menus
menus: dict[Menu] = {
    'public_menu': PublicMenu(),
    'private_menu': PrivateMenu()
}
