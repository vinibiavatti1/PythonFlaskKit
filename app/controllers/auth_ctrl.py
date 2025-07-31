from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash
from markupsafe import escape
from app.services import auth_service
from app.utils import hash_utils


auth_ctrl = Blueprint('auth_ctrl', __name__)


@auth_ctrl.route('/login', methods=['GET'])
def login():
    return render_template('/pages/login.html')


@auth_ctrl.route('/logout')
def logout():
    auth_service.logout()
    flash('Logout Success!', category='success')
    return redirect('/login')


@auth_ctrl.route('/login', methods=['POST'])
def login_action():
    email = escape(request.form.get('email'))
    password_hash = hash_utils.hash(request.form.get('password'))
    if auth_service.login(email, password_hash):
        flash('Login Success!', category='success')
        return redirect('/')
    else:
        flash('Invalid e-mail or password', category='danger')
        return render_template('/pages/login.html')
