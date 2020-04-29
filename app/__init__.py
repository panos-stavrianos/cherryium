# -*- coding: utf-8 -*-
import logging

from flask_babel import Babel
from flask_caching import Cache
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager
from gevent import monkey

monkey.patch_all()
from flask_socketio import SocketIO
from flask_minio import Minio
from flask_sqlalchemy_caching import CachingQuery

from flask import Flask, request, session

from app.config import Config

app = Flask(__name__, template_folder="templates")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object(Config)
storage = Minio(app)
babel = Babel(app)
logging.getLogger('sqlalchemy.engine.base.Engine').disabled = True


class CustomerQuery(CachingQuery):
    def by_user(self, current_user):
        modelClass = self._mapper_zero().class_
        return self.filter(modelClass.user == current_user)

    def by_id(self, record_id):
        modelClass = self._mapper_zero().class_
        return self.filter(modelClass.id == record_id)


db = SQLAlchemy(app, query_class=CustomerQuery)
migrate = Migrate(app, db)
cache = Cache(app)

socketio = SocketIO(app)

@babel.localeselector
def get_locale():
    try:
        language = session['language']
    except KeyError:
        language = None

    if language is not None and language != 'none' and language != 'None':
        return language

    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


from app import models

user_manager = UserManager(app, db, models.User)

from app.routes import routes, customers, products, services, expenses, partners, dashboard
