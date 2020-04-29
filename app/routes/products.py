from gettext import gettext

from datatables import ColumnDT, DataTables
from flask import render_template, request, redirect
from flask_user import login_required, current_user

from app import app, db
from app.forms import print_errors, ProductForm
from app.models import Product


@app.route('/products')
@login_required
def products_route():
    return render_template('products.html', page='products', title=gettext('Products'))


@app.route('/product/<product_id>')
@login_required
def product_route(product_id):
    product = Product.query.by_user(current_user).by_id(product_id).first()
    return render_template('product.html', page='products', title=gettext('Product'), product=product)


@app.route('/products_data')
@login_required
def products_data():
    columns = [
        ColumnDT(Product.id, mData='id'),
        ColumnDT(Product.name, mData='name'),
        ColumnDT(Product.description, mData='description'),
        ColumnDT(Product.price, mData='price'),
        ColumnDT(Product.enabled, mData='enabled')
    ]
    query = db.session.query().select_from(Product).filter(Product.user == current_user)
    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
    return rowTable.output_result()


@app.route('/product_add_edit/<record_id>', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def product_add_edit(record_id='0'):
    if record_id == '0':
        record = Product(user=current_user)
    else:
        record = Product.query.by_user(current_user).filter(
            Product.id == record_id).first()
    form = ProductForm(obj=record)
    try:
        form.populate_obj(record)
    except:
        pass
    if form.validate_on_submit():  # it's submit!
        db.session.add(record)
        db.session.commit()
        if record_id == '0':
            return redirect('/products')
        else:
            return redirect('/product/' + record_id)

    print_errors(form)
    return render_template('forms/product_modal.html', form=form, record=record)


@app.route('/delete_product/<record_id>', methods=['GET'])
@login_required
def delete_product(record_id):
    product = Product.query.by_user(current_user).filter(Product.id == record_id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect('/products')
