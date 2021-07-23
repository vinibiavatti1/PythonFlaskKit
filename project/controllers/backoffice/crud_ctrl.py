from flask import (
    Blueprint,
    render_template,
    abort,
    request,
    current_app,
    flash
)
from werkzeug.utils import redirect
from project.utils.security_utils import login_required
from project.definitions import cruds
from project.repositories import dynamic_form_repository


# Blueprint
blueprint = Blueprint('crud', __name__)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/<name>/form', defaults={'id': None}, methods=['GET'])
@blueprint.route('/<name>/form/<id>', methods=['GET'])
@login_required()
def index(name, id):
    if name not in cruds:
        abort(404)
    crud = cruds[name]
    db_table = crud.db_table
    crud_form = crud.build_form()
    crud_form_builded = crud_form.build()
    record_data = None
    if id:
        record_data = dynamic_form_repository.find_by_id(
            db_table,
            id,
            form_fields=[field.name for field in crud_form.fields]
        )
        if not record_data:
            flash(f'Resource not found with id: {id}')
            return redirect(f'/backoffice/dynamic_list/{name}')
        for field in crud_form_builded['fields']:
            field['default'] = record_data[0][field['name']]
    return render_template(
        '/backoffice/dynamic_form.html',
        form_data=crud_form,
        form_name=name,
        record_data=record_data,
        id=id
    )


@blueprint.route('/<name>/form/save', defaults={'id': None}, methods=['POST'])
@blueprint.route('/<name>/form/save/<id>', methods=['POST'])
@login_required()
def save(name, id):
    if name not in cruds:
        abort(404)
    form = cruds[name]
    table_name = form.db_table_name
    try:
        if id is not None:
            dynamic_form_repository.update(table_name, id, request.form)
        else:
            dynamic_form_repository.insert(table_name, request.form)
        return redirect('/')
    except Exception as err:
        msg = 'An error ocurred to persist dynamic data: \n' + str(err)
        current_app.logger.error(msg)
    abort(500)
