from gettext import gettext

from datatables import ColumnDT, DataTables
from flask import render_template, request, redirect
from flask_user import login_required, current_user

from app import app, db
from app.forms import ExpenseForm, print_errors
from app.models import Expense


@app.route('/expenses')
@login_required
def expenses_route():
    return render_template('expenses.html', page='expenses', title=gettext('Expenses'))


@app.route('/expense/<expense_id>')
@login_required
def expense_route(expense_id):
    expense = Expense.query.by_user(current_user).by_id(expense_id).first()
    return render_template('expense.html', page='expenses', title=gettext('Expense'), expense=expense)


@app.route('/expenses_data')
@login_required
def expenses_data():
    columns = [
        ColumnDT(Expense.id, mData='id'),
        ColumnDT(Expense.name, mData='name'),
        ColumnDT(Expense.price, mData='price'),
    ]
    query = db.session.query().select_from(Expense).filter(Expense.user == current_user)
    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
    return rowTable.output_result()


@app.route('/expense_add_edit/<record_id>', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def expense_add_edit(record_id='0'):
    if record_id == '0':
        record = Expense(user=current_user)
    else:
        record = Expense.query.by_user(current_user).filter(
            Expense.id == record_id).first()
    form = ExpenseForm(obj=record)
    try:
        form.populate_obj(record)
    except:
        pass
    if form.validate_on_submit():  # it's submit!
        db.session.add(record)
        db.session.commit()
        if record_id == '0':
            return redirect('/expenses')
        else:
            return redirect('/expense/' + record_id)

    print_errors(form)
    return render_template('forms/expense_modal.html', form=form, record=record)


@app.route('/delete_expense/<record_id>', methods=['GET'])
@login_required
def delete_expense(record_id):
    expense = Expense.query.by_user(current_user).filter(Expense.id == record_id).first()
    db.session.delete(expense)
    db.session.commit()
    return redirect('/expenses')
