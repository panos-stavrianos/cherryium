from gettext import gettext

from datatables import ColumnDT, DataTables
from flask import render_template, request, redirect
from flask_user import login_required, current_user

from app import app, db
from app.forms import CustomerForm, print_errors
from app.models import Customer


@app.route('/customers')
@login_required
def customers_route():
    return render_template('customers.html', page='customers', title=gettext('Customers'))


@app.route('/customer/<record_id>')
@login_required
def customer_route(record_id):
    customer = Customer.query.by_user(current_user).by_id(record_id).first()
    print(customer)
    return render_template('customer.html', page='customers', title=gettext('Customer'), customer=customer)


@app.route('/customers_data')
@login_required
def customers_data():
    columns = [
        ColumnDT(Customer.id, mData='id'),
        ColumnDT(Customer.name, mData='name'),
        ColumnDT(Customer.phone_1, mData='phone_1'),
        ColumnDT(Customer.phone_2, mData='phone_2'),
        ColumnDT(Customer.comment, mData='comment'),
        ColumnDT(Customer.sex, mData='sex'),
    ]
    query = db.session.query().select_from(Customer).filter(Customer.user == current_user)
    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
    return rowTable.output_result()


@app.route('/customer_add_edit/<record_id>', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def customer_add_edit(record_id='0'):
    if record_id == '0':
        record = Customer(user=current_user)
    else:
        record = Customer.query.by_user(current_user).filter(
            Customer.id == record_id).first()
    form = CustomerForm(obj=record)
    try:
        form.populate_obj(record)
    except:
        pass
    if form.validate_on_submit():  # it's submit!
        db.session.add(record)
        db.session.commit()
        if record_id == '0':
            return redirect('/customers')
        else:
            return redirect('/customer/' + record_id)

    print_errors(form)
    return render_template('forms/customer_modal.html', form=form, record=record)


@app.route('/delete_customer/<record_id>', methods=['GET'])
@login_required
def delete_customer(record_id):
    customer = Customer.query.by_user(current_user).filter(Customer.id == record_id).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect('/customers')
