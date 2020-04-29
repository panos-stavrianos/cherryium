from gettext import gettext

from datatables import ColumnDT, DataTables
from flask import render_template, request, redirect
from flask_user import login_required, current_user

from app import app, db
from app.forms import print_errors, PartnerForm
from app.models import Partner


@app.route('/partners')
@login_required
def partners_route():
    return render_template('partners.html', page='partners', title=gettext('Partners'))


@app.route('/partner/<partner_id>')
@login_required
def partner_route(partner_id):
    partner = Partner.query.by_user(current_user).by_id(partner_id).first()
    return render_template('partner.html', page='partners', title=gettext('Partner'), partner=partner)


@app.route('/partners_data')
@login_required
def partners_data():
    columns = [
        ColumnDT(Partner.id, mData='id'),
        ColumnDT(Partner.name, mData='name'),
        ColumnDT(Partner.phone, mData='phone'),
        ColumnDT(Partner.comment, mData='comment'),
        ColumnDT(Partner.enabled, mData='enabled')
    ]
    query = db.session.query().select_from(Partner).filter(Partner.user == current_user)
    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
    return rowTable.output_result()


@app.route('/partner_add_edit/<record_id>', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def partner_add_edit(record_id='0'):
    if record_id == '0':
        record = Partner(user=current_user)
    else:
        record = Partner.query.by_user(current_user).filter(
            Partner.id == record_id).first()
    form = PartnerForm(obj=record)
    try:
        form.populate_obj(record)
    except:
        pass
    if form.validate_on_submit():  # it's submit!
        db.session.add(record)
        db.session.commit()
        if record_id == '0':
            return redirect('/partners')
        else:
            return redirect('/partner/' + record_id)

    print_errors(form)
    return render_template('forms/partner_modal.html', form=form, record=record)


@app.route('/delete_partner/<record_id>', methods=['GET'])
@login_required
def delete_partner(record_id):
    partner = Partner.query.by_user(current_user).filter(Partner.id == record_id).first()
    db.session.delete(partner)
    db.session.commit()
    return redirect('/partners')
