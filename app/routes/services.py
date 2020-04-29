from gettext import gettext

from datatables import ColumnDT, DataTables
from flask import render_template, request, redirect
from flask_user import login_required, current_user

from app import app, db
from app.forms import print_errors, ServiceForm
from app.models import Service


@app.route('/services')
@login_required
def services_route():
    return render_template('services.html', page='services', title=gettext('Services'))


@app.route('/service/<service_id>')
@login_required
def service_route(service_id):
    service = Service.query.by_user(current_user).by_id(service_id).first()
    return render_template('service.html', page='services', title=gettext('Service'), service=service)


@login_required
@app.route('/services_data')
def services_data():
    columns = [
        ColumnDT(Service.id, mData='id'),
        ColumnDT(Service.name, mData='name'),
        ColumnDT(Service.description, mData='description'),
        ColumnDT(Service.price, mData='price'),
        ColumnDT(Service.enabled, mData='enabled')
    ]
    query = db.session.query().select_from(Service).filter(Service.user == current_user)
    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
    return rowTable.output_result()


@app.route('/service_add_edit/<record_id>', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def service_add_edit(record_id='0'):
    if record_id == '0':
        record = Service(user=current_user)
    else:
        record = Service.query.by_user(current_user).filter(
            Service.id == record_id).first()
    form = ServiceForm(obj=record)
    try:
        form.populate_obj(record)
    except:
        pass
    if form.validate_on_submit():  # it's submit!
        db.session.add(record)
        db.session.commit()
        if record_id == '0':
            return redirect('/services')
        else:
            return redirect('/service/' + record_id)

    print_errors(form)
    return render_template('forms/service_modal.html', form=form, record=record)


@app.route('/delete_service/<record_id>', methods=['GET'])
@login_required
def delete_service(record_id):
    service = Service.query.by_user(current_user).filter(Service.id == record_id).first()
    db.session.delete(service)
    db.session.commit()
    return redirect('/services')
