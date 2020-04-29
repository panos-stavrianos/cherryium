# -*- coding: utf-8 -*-
import time

from flask import flash
from flask_babel import gettext
from flask_sqlalchemy_caching import FromCache
from flask_user import current_user
from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, SelectField
from wtforms_alchemy import model_form_factory

from app import cache
from app.ExtraFields import EnumField
from app.models import Customer, SexType, Expense, Partner, Product, Service, Discount

BaseModelForm = model_form_factory(FlaskForm)


def get_partners_as_choices():
    return list(map(lambda record: (str(record.id), record.name),
                    Partner.query.by_user(current_user).options(FromCache(cache)).all()))


def get_customers_as_choices():
    return list(map(lambda record: (str(record.id), record.name),
                    Customer.query.by_user(current_user).options(FromCache(cache)).all()))


def get_discounts_as_choices():
    return list(map(lambda record: (str(record.id), record.name + " - " + record.per_cent),
                    Discount.query.by_user(current_user).options(FromCache(cache)).all()))


def get_services_as_choices():
    return list(
        map(lambda record: (str(record.id), "{} - {} - {}€".format(record.name, record.description, record.price)),
            Service.query.by_user(current_user).options(FromCache(cache)).all()))


def get_products_as_choices():
    return list(
        map(lambda record: (str(record.id), "{} - {} - {}€".format(record.name, record.description, record.price)),
            Product.query.by_user(current_user).options(FromCache(cache)).all()))


class SaleForm(Form):
    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        t0 = time.time()

        self.customer.choices = get_customers_as_choices()
        self.partner.choices = get_partners_as_choices()
        self.discount.choices = get_discounts_as_choices()

        t1 = time.time()
        print("TIME DIF", t1 - t0)

    customer = SelectField(gettext('Customer'))
    partner = SelectField(gettext('Partner'))
    discount = SelectField(gettext('Discount'))
    # locations = FieldList(FormField(LocationForm), min_entries=2)
    submit = SubmitField(gettext('Submit'))


class CustomerForm(BaseModelForm):
    class Meta:
        model = Customer

    sex = EnumField(SexType)
    submit = SubmitField(gettext('Submit'))


class ExpenseForm(BaseModelForm):
    class Meta:
        model = Expense

    submit = SubmitField(gettext('Submit'))


class PartnerForm(BaseModelForm):
    class Meta:
        model = Partner

    submit = SubmitField(gettext('Submit'))


class ProductForm(BaseModelForm):
    class Meta:
        model = Product

    submit = SubmitField(gettext('Submit'))


class ServiceForm(BaseModelForm):
    class Meta:
        model = Service

    submit = SubmitField(gettext('Submit'))


def flash_errors(form):
    for field, errors in form.errors.items():
        flash('\n'.join(errors), category='danger')


def print_errors(form):
    for field, errors in form.errors.items():
        print(field, '\n'.join(errors))
