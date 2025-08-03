from flask import Blueprint, render_template


register_ctrl = Blueprint('register_ctrl', __name__)


@register_ctrl.route('/register')
def index() -> str:
    return render_template('/pages/register.html')
