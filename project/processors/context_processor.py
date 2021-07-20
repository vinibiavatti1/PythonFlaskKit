from flask import Blueprint, request
from project.config.config import config
from project.dictionaries.dictionary import get_dictionary


# Blueprint
blueprint = Blueprint('context_processors', __name__)


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
    Inject the dictionary by the defined lang in cookies
    If no lang was defined, the default dictionary will be used
    """
    lang = request.cookies.get('lang', None)
    dictionary = get_dictionary(lang)
    return dict(dictionary=dictionary)
