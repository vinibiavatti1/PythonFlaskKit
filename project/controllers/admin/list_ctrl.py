from flask import Blueprint, render_template
from project.utils.security_utils import login_required


# Blueprint
blueprint = Blueprint('list', __name__, url_prefix='/admin/list')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    headers = ['#', 'Product', 'Location', 'Price', 'Actions']
    data = [
        (1, 'Laptop', 'Lisbon', '$ 999.00', '<a href="#!">Details</a>'),
        (2, 'Smartphone', 'New York', '$ 699.00', '<a href="#!">Details</a>'),
        (3, 'Monitor', 'Rio', '$ 100.00', '<a href="#!">Details</a>'),
        (4, 'Coffee', 'Paris', '$ 1.99', '<a href="#!">Details</a>'),
        (5, 'Guitar', 'London', '$ 80.00', '<a href="#!">Details</a>'),
    ]
    return render_template(
        '/admin/list.html',
        headers=headers,
        data=data
    )
