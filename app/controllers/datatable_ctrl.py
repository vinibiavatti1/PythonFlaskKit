from flask import Blueprint, render_template


datatable_ctrl = Blueprint('datatable_ctrl', __name__)


@datatable_ctrl.route('/datatable')
def index() -> str:
    data = [
        (1, 'John Duo', 'Lorem Ipsum', True, '15-10-2025'),
        (2, 'Jane Doe', 'Dolor sit amet', False, '18-10-2025'),
        (3, 'Peter Pan', 'Consectetur adipiscing', True, '22-10-2025'),
        (4, 'Mary Jane', 'Sed do eiusmod', True, '25-10-2025'),
        (5, 'Bruce Wayne', 'Tempor incididunt', False, '01-11-2025'),
        (6, 'Clark Kent', 'Ut labore et dolore', True, '05-11-2025'),
        (7, 'Diana Prince', 'Magna aliqua', True, '10-11-2025'),
        (8, 'Tony Stark', 'Ut enim ad minim veniam', False, '14-11-2025'),
        (9, 'Steve Rogers', 'Quis nostrud exercitation', True, '19-11-2025'),
        (10, 'Natasha Romanoff', 'Ullamco laboris nisi', True, '23-11-2025'),
        (11, 'Thor Odinson', 'Ex ea commodo consequat', False, '28-11-2025'),
        (12, 'Bruce Banner', 'Duis aute irure dolor', True, '02-12-2025'),
        (13, 'Wanda Maximoff', 'In reprehenderit in voluptate', True, '07-12-2025'),
        (14, 'Vision', 'Velit esse cillum dolore', False, '11-12-2025'),
        (15, 'Stephen Strange', 'Eu fugiat nulla pariatur', True, '16-12-2025'),
    ]
    return render_template(
        '/pages/datatable.html',
        data=data
    )
