# -*- coding: utf-8 -*-

import pandas as pd

from app import app, db
from app.models import Partner, Product, Customer, Discount, Expense, Service, CustomerProduct, \
    CustomerService


# noinspection PyArgumentList
@app.route('/update_partners')
def update_partners():
    df = pd.read_csv('/home/panos/Documents/Hair&Flair/dump/dump2/heroku_f61548274275106_partners.tsv', sep=';')
    print(df.head(0))
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        record = Partner(
            id=row['id'],
            name=row['name'],
            phone=row['phone'],
            comment=row['comment'],
            enabled=row['enabled'],
            user_id=row['user_id'],
            created_at=row['created_at'],
            updated_at=row['updated_at'])
        db.session.add(record)
        db.session.commit()

    return "OK"


# noinspection PyArgumentList
@app.route('/update_products')
def update_products():
    df = pd.read_csv('/home/panos/Documents/Hair&Flair/dump/dump2/heroku_f61548274275106_products.tsv', sep=';')
    print(df.head(0))
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        record = Product(
            id=row['id'],
            name=row['name'],
            description=row['description'],
            price=row['price'],
            user_id=row['user_id'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            enabled=row['enabled'])
        db.session.add(record)
        db.session.commit()

    return "OK"


# noinspection PyArgumentList
@app.route('/update_customers')
def update_customers():
    df = pd.read_csv('/home/panos/Documents/Hair&Flair/dump/dump2/heroku_f61548274275106_customers.tsv', sep=';')
    print(df.head(0))
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        record = Customer(
            id=row['id'],
            name=row['name'],
            phone_1=row['phone_1'],
            phone_2=row['phone_2'],
            user_id=row['user_id'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            sex=row['sex'] + 1)
        db.session.add(record)
        db.session.commit()

    return "OK"


# noinspection PyArgumentList
@app.route('/update_discounts')
def update_discounts():
    df = pd.read_csv('/home/panos/Documents/Hair&Flair/dump/dump2/heroku_f61548274275106_discounts.tsv', sep=';')
    print(df.head(0))
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        record = Discount(
            id=row['id'],
            name=row['name'],
            per_cent=row['per_cent'],
            user_id=row['user_id'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            enabled=row['enabled'])
        db.session.add(record)
    db.session.commit()

    return "OK"


# noinspection PyArgumentList
@app.route('/update_expenses')
def update_expenses():
    df = pd.read_csv('/home/panos/Documents/Hair&Flair/dump/dump2/heroku_f61548274275106_expenses.tsv', sep=';')
    print(df.head(0))
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        record = Expense(
            id=row['id'],
            name=row['name'],
            price=row['price'],
            user_id=row['user_id'],
            created_at=row['created_at'],
            updated_at=row['updated_at'])
        db.session.add(record)
    db.session.commit()

    return "OK"


# noinspection PyArgumentList
@app.route('/update_services')
def update_services():
    df = pd.read_csv('/home/panos/Documents/Hair&Flair/dump/dump2/heroku_f61548274275106_services.tsv', sep=';')
    print(df.head(0))
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        record = Service(
            id=row['id'],
            name=row['name'],
            description=row['description'],
            price=row['price'],
            user_id=row['user_id'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            enabled=row['enabled'],
        )
        db.session.add(record)
    db.session.commit()

    return "OK"


# noinspection PyArgumentList
@app.route('/update_customer_products')
def update_customer_products():
    df = pd.read_csv('/home/panos/Documents/Hair&Flair/dump/dump2/heroku_f61548274275106_customer_products.tsv',
                     sep=';')
    print(df.head(0))
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        record = CustomerProduct(
            id=row['id'],
            customer_id=row['customer_id'],
            product_id=row['product_id'],
            user_id=row['user_id'],
            amount=row['amount'],
            price=row['price'],
            comment=row['comment'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            discount_id=row['discount_id'],
            partner_id=row['partner_id'],
            discount_per_cent=row['discount_per_cent'])
        db.session.add(record)
    db.session.commit()

    return "OK"


# noinspection PyArgumentList
@app.route('/update_customer_services')
def update_customer_services():
    df = pd.read_csv('/home/panos/Documents/Hair&Flair/dump/dump2/heroku_f61548274275106_customer_services.tsv',
                     sep=';')
    print(df.head(0))
    df = df.where(pd.notnull(df), None)

    for index, row in df.iterrows():
        record = CustomerService(
            id=row['id'],
            customer_id=row['customer_id'],
            service_id=row['service_id'],
            user_id=row['user_id'],
            amount=row['amount'],
            price=row['price'],
            comment=row['comment'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            discount_id=row['discount_id'],
            partner_id=row['partner_id'],
            discount_per_cent=row['discount_per_cent'])
        db.session.add(record)
    db.session.commit()

    return "OK"
