# Python Flask Kit
The Python Flask Kit is a starter kit with util pre-implemented features for [Python Flask](https://flask.palletsprojects.com/en/2.0.x/) projects that follow concepts of MVC. It uses the [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) library to render HTML templates. This kit includes a collections of utilities, default patterns, configurations, and pre defined plugins. You can also find internationalization classes in the kit to develop a multi-cultural application. The purpose of the kit is to facilitate our development and give it to us as a base for our projects. It is not a framework, it is just a library to help us a lot!

## Installation
The Python 3 is required for this project. Download or clone this repository in your project diretory and install the Python Environment and the dependencies of the project by executing the `run_setup.bat` file. This file will create a new Python environment in `.env` folder, and use `pip` to install the dependencies. To start the server, just execute `run_flask_dev.bat`, `run_flask_test.bat` or `run_flask_prod.bat` depending on the environment you want to start the application on.

## Configuration
There are three config files in the `/project/configs` directory. Each one corresponds to a specific environment. For example, if you run the `run_flask_test.bat` file, the `config_test.py` file will be used to define the configurations.

## Resources
The project is separated by areas that contains a specific type of resource. Check below some lists of the contents of the directories and a small description about the project files: 

### Project Files

File|Description
---|---
`blueprints.py`|Python flask entities register module
`config.py`|Configuration handler by environment
`errors.py`|Application error classes
`handlers.py`|HTTP error handlers
`i18n.py`|Internationalization utils
`menus.py`|Sidebar menus registration
`processors.py`|Jinja context processors

### Project Directories

Directory|Description
---|---
`/configs`|Configuration files for each environment
`/controllers`|Route controllers
`/enums`|Enumerations
`/models`|Data classes
`/repositories`|Database management functions 
`/services`|Business rules functions
`/translations`|Translation dictionaries for each idiom
`/utils`|Common application functions
`/validators`|Data validators functions

### Templates Directories

Directory|Description
---|---
`/admin`|Templates for authenticated users
`/errors`|HTTP error templates
`/macros`|Macro templates ("DRY" concept)
`/private`|Owner templates
`/public`|Templates for no authenticated users 

### Static Directories

Directory|Description
---|---
`/documents`|Text files
`/medias`|Media files
`/plugins`|External libraries
`/scripts`|JS files
`/styles`|CSS files

## Utils
The util modules have default functionalities for usage in entire of application. There are different kinds of utils that can be used for specified operation. Check the table below for more details:

Util|Definition
---|---
`cookie_utils.py`|Functions to work with cookies
`ctrl_utils.py`|Controller util functionalities
`database_utils.py`|Database manipulation functions
`datetime_utils.py`|Date and datetime functions
`mail_utils.py`|Mail sender functions
`security_utils.py`|Security and authentication routines
`translation_utils.py`|Internationalization functions

## Blueprints
The blueprints are resources that can be registered into Python Flask Engine, such as controllers, processors, etc. The file `project/blueprints.py` contains a list of blueprints that will be registered automatically when the application is running. New blueprints should be put inside this list.

## Context Processors
Context processors are routines that will be called before rendering the Jinja templates, in order to define some global properties to be allowed for usage on the HTML templates. These routines can be found at `/project/processors.py` file.

## Internationalization
You can define multiple translation files in `/project/translations` directory. These translation files uses a Python Dictionary, where each application message has its own key, and this key will be allowed for usage on templates by a Context Processor function called `inject_dictionary()`. The translation dictionary will be injected to Jinja templates depending on the idiom defined in the website `lang` cookie, so, if the lang cookie is defined with `en_us` value, the `en_us.py` dictionary will be injected by the Context Processor. The translation dictionary keys are located in a variable called `i18n`. For example, you can render the welcome message in HTML file by coding:
```jinja
<p>{{ i18n.general.welcome }}</p>
```  

## Layout
The `layout.html` file is the base file that is used to render any template of the website. All templates should extend the layout file. In layout, some macros are imported and rendered automatically. The CSS, JS and metatags are defined into the `/macros/headers.html` file. Any new library that need to be imported to the website should be defined into this file.

## Macros
Macro is a HTML file with the contents defined inside functions. It allows developer to create common templates that could be used in different parts of the application. Some parameters can be defined for these functions to handle the macro templates dinamically. They are useful to put often used idioms into reusable functions to not repeat yourself ("DRY").

```jinja
{# Alert Macro #}
{% macro alert(message, type, dismissible = true) %}
    <div class="alert alert-{{type}} {{ 'alert-dismissible' if dismissible else '' }}">
        {{message}}
        {% if dismissible %}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        {% endif %}
    </div>
{% endmacro %}

{# Usage example #}
{{ alert('Hello world!', 'success') }}
```

## Thanks
I hope this lib can help you to start any Python Flask project you want. Thanks!
