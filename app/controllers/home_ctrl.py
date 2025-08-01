from flask import Blueprint, render_template


home_ctrl = Blueprint('home_ctrl', __name__)


@home_ctrl.route('/')
def index() -> str:
    return render_template('/pages/home.html')
