from flask import Blueprint, render_template, request


# Blueprint
blueprint = Blueprint('search', __name__, url_prefix='/search')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
def index():
    query = request.args.get('query')
    results = [
        {
            'title': 'Lorem ipsum',
            'description': 'Suspendisse aliquet egestas justo consectetur.',
            'link': '/',
        },
        {
            'title': 'Suspendisse eget',
            'description': 'Aenean pharetra pretium nunc.',
            'link': '/',
        },
        {
            'title': 'Phasellus tincidunt',
            'description': 'Fusce varius convallis nunc sed aliquet.',
            'link': '/',
        }
    ]
    return render_template(
        '/public/search.html',
        query=query,
        results=results
    )
