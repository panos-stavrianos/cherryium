# -*- coding: utf-8 -*-

import enum

from flask_babel import gettext
from flask_user import UserMixin

from app import db


class Base(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


# Define User data-model
class User(Base, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean(), default=True)
    name = db.Column(db.String(50), default='', nullable=True)
    logo = db.Column(db.String(250), default='', nullable=True)

    products = db.relationship("Product")
    services = db.relationship("Service")
    discounts = db.relationship("Discount")
    partners = db.relationship("Partner")
    expenses = db.relationship("Expense")
    customers = db.relationship("Customer")
    customer_products = db.relationship("CustomerProduct")
    customer_services = db.relationship("CustomerService")


# Define the Role data-model
class Role(Base):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(Base):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


def ADMIN():
    return Role.query.filter_by(name='admin').first()


def OWNER():
    return Role.query.filter_by(name='owner').first()


def USER():
    return Role.query.filter_by(name='user').first()


class Product(Base):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0.0)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')


class Service(Base):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0.0)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')


class Discount(Base):
    __tablename__ = 'discounts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    per_cent = db.Column(db.Float, nullable=False, default=0.0)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')


class Partner(Base):
    __tablename__ = 'partners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), nullable=True)
    comment = db.Column(db.String(255), nullable=True)
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')


class SexType(enum.IntEnum):
    male = 1
    female = 2

    def __str__(self):
        return gettext("Male") if self.value == 1 else gettext("Female")


class Customer(Base):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    phone_1 = db.Column(db.String(255), nullable=True)
    phone_2 = db.Column(db.String(255), nullable=True)
    comment = db.Column(db.String(255), nullable=True)

    sex = db.Column(db.Enum(SexType), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')


class Expense(Base):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False, default=0.0)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')


class CustomerProduct(Base):
    __tablename__ = 'customer_products'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Float, nullable=False, default=0.0)
    discount_per_cent = db.Column(db.Float, nullable=False, default=0.0)
    comment = db.Column(db.String(255), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    discount_id = db.Column(db.Integer, db.ForeignKey('discounts.id'), nullable=False)
    partner_id = db.Column(db.Integer, db.ForeignKey('partners.id'), nullable=False)


class CustomerService(Base):
    __tablename__ = 'customer_services'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Float, nullable=False, default=0.0)
    discount_per_cent = db.Column(db.Float, nullable=False, default=0.0)
    comment = db.Column(db.String(255), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'))
    discount_id = db.Column(db.Integer, db.ForeignKey('discounts.id'))
    partner_id = db.Column(db.Integer, db.ForeignKey('partners.id'))


def create_tables():
    db.create_all()

# create_tables()
# print("Hello")
