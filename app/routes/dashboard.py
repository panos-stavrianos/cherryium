from gettext import gettext

from datatables import ColumnDT, DataTables
from flask import render_template, request, redirect
from flask_user import login_required, current_user
from sqlalchemy import literal
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import ClauseElement

from app import app, db
from app.forms import SaleForm
from app.models import CustomerProduct, Customer, Product, CustomerService, Service


@app.route('/')
@login_required
def dashboard():
    if current_user:
        print(current_user)
        return render_template('dashboard.html', page='dashboard', title=gettext('Dashboard'))
    else:
        return redirect("/user/sign-in")


@app.route('/customer_products_data')
@login_required
def customer_products_data():
    columns = [
        ColumnDT(CustomerProduct.id, mData='id'),
        ColumnDT(CustomerProduct.customer_id, mData='customer_id'),
        ColumnDT(Customer.name, mData='customer_name'),
        ColumnDT(CustomerProduct.product_id, mData='product_id'),
        ColumnDT(Product.name, mData='product_name'),
        ColumnDT(Product.description, mData='product_description'),
        ColumnDT(CustomerProduct.created_at, mData='created_at')
    ]
    query = db.session.query().select_from(CustomerProduct) \
        .join(Customer).join(Product).filter(CustomerProduct.user == current_user)

    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
    return rowTable.output_result()


@app.route('/customer_services_data')
@login_required
def customer_services_data():
    columns = [
        ColumnDT(CustomerService.id, mData='id'),
        ColumnDT(CustomerService.customer_id, mData='customer_id'),
        ColumnDT(Customer.name, mData='customer_name'),
        ColumnDT(CustomerService.service_id, mData='service_id'),
        ColumnDT(Service.name, mData='service_name'),
        ColumnDT(Service.description, mData='service_description'),
        ColumnDT(CustomerService.created_at, mData='created_at')
    ]
    query = db.session.query().select_from(CustomerService) \
        .join(Customer).join(Service).filter(CustomerService.user == current_user)

    params = request.args.to_dict()
    rowTable = DataTables(params, query, columns)
    return rowTable.output_result()


class Match(ClauseElement):
    def __init__(self, columns, value):
        self.columns = columns
        self.value = literal(value)


@compiles(Match)
def _match(element, compiler, **kw):
    return "MATCH ({}) AGAINST ({} IN BOOLEAN MODE)".format(
        ", ".join(compiler.process(c, **kw) for c in element.columns),
        compiler.process(element.value))


@app.route('/search', strict_slashes=True, methods=['POST'])
@login_required
def search():
    search_query = request.json['search']
    customers = db.session.query(Customer).by_user(current_user).filter(
        Match([Customer.name, Customer.phone_1, Customer.phone_2, Customer.comment], search_query + "*")).limit(5).all()
    services = db.session.query(Service).by_user(current_user).filter(
        Match([Service.name, Service.description], search_query + "*")).limit(5).all()
    products = db.session.query(Product).by_user(current_user).filter(
        Match([Product.name, Product.description], search_query + "*")).limit(5).all()
    print(customers)
    print(services)
    print(products)
    return render_template('forms/search_results.html', customers=customers, services=services, products=products)


@app.route('/new_sale', strict_slashes=False, methods=['GET', 'POST'])
@login_required
def new_sale():
    form = SaleForm()

    if form.validate_on_submit():  # it's submit!
        # db.session.add(record)
        # db.session.commit()
        # if record_id == '0':
        #     return redirect('/partners')
        # else:
        #     return redirect('/partner/' + record_id)
        print(form.data)

    return render_template('forms/new_sale.html', form=form)
