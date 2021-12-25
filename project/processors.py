from project.utils.security_utils import is_authenticated, has_permission
from project.utils.cookie_utils import cookie_policy_consent
from flask import Blueprint
from project.config import config
from project.utils.translation_utils import get_translations, get_locales
from project.i18n import translations_dict
from project import menus
from project.enums.permission_enum import PermissionEnum


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
    return dict(
        i18n=get_translations(),
        locales=get_locales(),
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
        cookie_policy_consent=cookie_policy_consent()
    )


@blueprint.app_context_processor
def inject_menu():
    """
    Inject the sidenav menus by user authentication
    """
    menu = None
    if has_permission(PermissionEnum.ADMIN.value):
        menu = menus.build_admin_manu()
    elif has_permission(PermissionEnum.MEMBER.value):
        menu = menus.build_private_menu()
    else:
        menu = menus.build_public_menu()
    return dict(menu=menu)
