# -*- coding: utf-8 -*-
import json

from flask import send_from_directory, render_template, get_flashed_messages, request, redirect, session
from flask_babel import gettext
from flask_user import current_user

from app import app, babel, storage


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(request.referrer)


@app.route('/flash_messages')
def flash_messages():
    messages = get_flashed_messages(with_categories=True)

    messages_json = []
    for category, message in messages:
        if category == 'error':
            category = 'danger'
        messages_json.append({"content": {"icon": "now-ui-icons ui-1_bell-53", "message": gettext(message)},
                              "options": {"type": category, "timer": 8000,
                                          "placement": {"from": "bottom", "align": "right"}}})

    return {'messages': messages_json}


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.context_processor
def utility_processor():
    return dict(lang=babel.locale_selector_func())


@app.route('/upload')
def upload_file():
    # res = storage.connection.fput_object('hair-flair', 'routes.py', 'app/routes/routes.py')
    # res = storage.connection.get_object('hair-flair', 'd05b9dacdfab91555e36430f93c3e0c7-1')
    # res = storage.connection.get_object('hair-flair', 'Dub.jpg')
    # res = storage.connection.list_objects('hair-flair')
    objects = storage.connection.get_bucket_policy('hair-flair')
    parsed = json.loads(objects)
    # print(json.dumps(objects, indent=4, sort_keys=True))
    return "<img src='https://orbit-bucket.app.orbitsystems.gr/hair-flair/Dub.jpg'/>"
