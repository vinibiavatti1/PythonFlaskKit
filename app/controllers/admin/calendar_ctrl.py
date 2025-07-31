from flask import Blueprint, render_template
from json import dumps
from app.utils.security_utils import login_required


# Blueprint
blueprint = Blueprint('calendar', __name__, url_prefix='/admin/calendar')


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    events = [
        {
            'title': 'All Day Event',
            'start': '2021-12-29',
        },
        {
            'title': 'Long Event',
            'start': '2021-12-06',
            'end': '2021-12-09',
        },
        {
            'groupId': '999',
            'title': 'Repeating Event',
            'start': '2021-12-03T23:00:00',
        },
        {
            'groupId': '999',
            'title': 'Repeating Event',
            'start': '2022-01-03T16:00:00',
        },
        {
            'title': 'Conference',
            'start': '2021-01-02',
            'end': '2021-01-03',
        },
        {
            'title': 'Meeting',
            'start': '2021-01-12T10:30:00',
            'end': '2021-01-12T12:30:00',
        },
        {
            'title': 'Click for Google',
            'start': '2021-12-16',
            'url': 'http://google.com/',
        }
    ]
    return render_template(
        '/admin/calendar.html',
        json_events=dumps(events),
    )
