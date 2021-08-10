from project.utils.security_utils import is_authenticated, has_permission
from project.utils.cookie_utils import cookie_policy_accepted
from flask import Blueprint
from project.config import config
from project.utils.translation_utils import get_dictionary
from project.dictionaries import dictionaries
from project import menus
from project.enums import permission_enum


# Blueprint
blueprint = Blueprint('processors', __name__)


###############################################################################
# Processors
###############################################################################


@blueprint.app_context_processor
def inject_configuration():
    """
    Inject the environment configuration to Jinja template data
    """
    return dict(config=config)


@blueprint.app_context_processor
def inject_dictionary():
    """
    Inject the dictionary by the defined locale in cookies
    If no locale was defined, the default dictionary will be used. If the flag
    "i18n" in config is defined to False, the dictionary will not be injected
    """
    if not config['i18n']:
        return
    dictionary = get_dictionary()
    locales = [k for k in dictionaries.keys() if k != 'default']
    return dict(
        dictionary=dictionary,
        i18n=dictionary,
        locales=locales
    )


@blueprint.app_context_processor
def inject_resources():
    """
    Inject common resources to be used in Jinja templates
    """
    return dict(
        isinstance=isinstance,
        zip=zip,
        is_authenticated=is_authenticated,
        cookie_policy_accepted=cookie_policy_accepted()
    )


@blueprint.app_context_processor
def inject_menu():
    """
    Inject the sidenav menus by user authentication
    """
    menu = None
    if has_permission(permission_enum.ADMIN):
        menu = menus.build_admin_manu()
    elif has_permission(permission_enum.MEMBER):
        menu = menus.build_private_menu()
    else:
        menu = menus.build_public_menu()
    return dict(menu=menu)
