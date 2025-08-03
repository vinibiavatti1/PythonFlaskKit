from flask import Blueprint, render_template


map_ctrl = Blueprint('map_ctrl', __name__)


@map_ctrl.route('/map')
def index() -> str:
    return render_template(
        '/pages/map.html',
        points=[(38.73, -9.14)],
        lat=38.73,
        lng=-9.14,
        zoom=12
    )
