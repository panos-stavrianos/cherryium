# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'AK2z8RvgrN3rvk4WKBSDGsU7LKkwGdRP'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql://root:NA5y2ES5SAFnkGXA@192.168.111.13:33306/hair_flair'

    MYSQL_DATABASE_CHARSET = 'utf8mb4'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300

    # Flask-User settings
    USER_APP_NAME = "Hair&Flair"  # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True  # Disable email authentication
    USER_ENABLE_USERNAME = False  # Enable username authentication
    USER_ENABLE_REGISTER = True
    USER_REQUIRE_RETYPE_PASSWORD = True  # Simplify register form
    USER_ENABLE_INVITE_USER = False

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'mail.orbitsystems.gr'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'hairnflair@orbitsystems.gr'
    MAIL_PASSWORD = 'd8ZdfB{(HPrA'
    MAIL_DEFAULT_SENDER = '"Hair&Flair" <hairnflair@orbitsystems.gr>'

    LANGUAGES = {
        'en': 'English',
        'el_GR': 'Greek'
    }

    MINIO_ENDPOINT = '192.168.111.13:9001'
    MINIO_ACCESS_KEY = 'orbit'
    MINIO_SECRET_KEY = '326505osnet'
    MINIO_SECURE = False
    MINIO_REGION = None
    MINIO_HTTP_CLIENT = None
