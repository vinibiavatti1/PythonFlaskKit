from project.services.auth_service import is_authenticated
from flask import Blueprint
from project.config.config import config
from project.utils.translation_utils import get_dictionary
from project.dictionaries.registry import dictionaries
from project.menus.registry import menus


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
    If no locale was defined, the default dictionary will be used
    """
    dictionary = get_dictionary()
    locales = [k for k in dictionaries.keys() if k != 'default']
    return dict(
        dictionary=dictionary,
        locales=locales
    )


@blueprint.app_context_processor
def inject_common_functions():
    """
    Inject common functions to be used in Jinja templates
    """
    return dict(
        zip=zip,
        is_authenticated=is_authenticated
    )


@blueprint.app_context_processor
def inject_menus():
    """
    Inject the sidenav menus by user authentication
    """
    for menu in menus.values():
        if menu.rule():
            options = menu.build().get_options()
            return dict(menu=options)
