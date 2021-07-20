from flask import Flask, request
from flask.templating import render_template
from markupsafe import escape
from project.config.config import config
from project.dictionaries.dictionary import get_dictionary
from project.routes.user import blueprint as user_blueprint
from project.routes.homepage import blueprint as homepage_blueprint
from project.routes.locale import blueprint as locale_blueprint


# Init flask
app = Flask(__name__)


# Register blueprints
app.register_blueprint(user_blueprint)
app.register_blueprint(homepage_blueprint)
app.register_blueprint(locale_blueprint)


# Context processors
@app.context_processor
def inject_configuration():
    return dict(config=config)


@app.context_processor
def inject_dictionary():
    lang = request.cookies.get('lang', None)
    dictionary = get_dictionary(lang)
    return dict(dictionary=dictionary)


# Errors handler
@app.errorhandler(404)
def not_found(error_message):
    return render_template('errors/404.html', error_message=error_message)
