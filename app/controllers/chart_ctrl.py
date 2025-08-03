from flask import Blueprint, render_template
import json


chart_ctrl = Blueprint('chart_ctrl', __name__)


@chart_ctrl.route('/chart')
def index() -> str:
    chart_data = {
        'labels': (
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July'
        ),
        'datasets': [{
            'label': 'Data',
            'data': (2, 5, 1, 10, 4, 7, 6),
            'backgroundColor': (
                'rgba(255, 99, 132, 0.5)',
                'rgba(255, 159, 64, 0.5)',
                'rgba(255, 205, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(201, 203, 207, 0.5)'
            ),
            'borderColor': (
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255',
                'rgb(201, 203, 207'
            ),
            'borderWidth': 2
        }]
    }
    return render_template(
        '/pages/chart.html',
        json_data=json.dumps(chart_data)
    )
