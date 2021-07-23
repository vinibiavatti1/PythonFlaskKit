from flask import Blueprint, render_template
from project.models.chart_models import Chart, ChartDataset
from project.utils.security_utils import login_required


# Blueprint
blueprint = Blueprint('chart', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index():
    # Create chart data
    chart_data = Chart([
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July'
    ])

    # Create dataset
    chart_dataset = ChartDataset('Data')
    chart_dataset.set_data((2, 5, 1, 10, 4, 7, 6))
    chart_dataset.set_background_colors((
        'rgba(255, 99, 132, 0.5)',
        'rgba(255, 159, 64, 0.5)',
        'rgba(255, 205, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(201, 203, 207, 0.5)',
    ))
    chart_dataset.set_border_colors((
        'rgb(255, 99, 132)',
        'rgb(255, 159, 64)',
        'rgb(255, 205, 86)',
        'rgb(75, 192, 192)',
        'rgb(54, 162, 235)',
        'rgb(153, 102, 255',
        'rgb(201, 203, 207',
    ))
    chart_data.add_dataset(chart_dataset)

    # Render
    return render_template(
        '/backoffice/chart.html',
        chart_type='bar',
        json_data=chart_data.to_json()
    )
