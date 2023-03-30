import os, sys
import json
from os import environ as env
from dotenv import load_dotenv, find_dotenv

from flask import Flask, Blueprint, \
    render_template, request, redirect, url_for, \
    abort, session, \
    make_response, Response, \
    jsonify, send_from_directory, logging

from flask_wtf.csrf import CSRFProtect
from flask_session import Session


app = Flask(__name__)

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
app.secret_key = env.get("APP_SECRET_KEY")
app.config['AUTH0_DOMAIN'] = env.get("AUTH0_DOMAIN")    
app.config['API_IDENTIFIER'] = env.get("API_IDENTIFIER") 
app.config['AUTH0_CLIENT_ID'] = env.get("AUTH0_CLIENT_ID")
app.config['AUTH0_CLIENT_SECRET'] = env.get("AUTH0_CLIENT_SECRET")
app.config['ALGORITHMS'] = json.loads(env.get('ALGORITHMS'))


class Blueprint_host(Blueprint):
    def __init__(self, *args, **kwargs):
        self.default_host = kwargs.pop('default_host', None)
        Blueprint.__init__(self, *args, **kwargs)

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        options['host'] = options.pop('host', self.default_host)
        super().add_url_rule(self, rule, endpoint=None, view_func=None, **options)


# csrf_protect = CSRFProtect()
# csrf_protect._exempt_views.add('dash.dash.dispatch')
# csrf_protect.init_app(app)
# jwt = JWTManager(app)

# redis_store = FlaskRedis()
# redis_store.init_app(app)

# redis_db = redis.Redis()  # host='localhost', port=6379,  db=0

# # cache = Cache(config=app.config['CACHE_CONFIG'])
# from flask_caching import Cache

# CACHE_CONFIG = {
#     # try 'filesystem' if you don't want to setup redis
#     'CACHE_TYPE': 'redis',
#     'CACHE_REDIS_URL': 'redis://localhost:6379'
# }
# cache = Cache(config=CACHE_CONFIG)
# cache.init_app(app)

from apps.authentication import auth
from apps.api import app_api
from apps.login import app_login
from apps.tests import app_test


app.register_blueprint(app_test, url_prefix='/tests')
app.register_blueprint(app_api, url_prefix='/api')
app.register_blueprint(app_login, url_prefix='/')


# @app.before_request
# def before_request():
#     if 'data' not in session:
#         session['data'] = {}
#     session['before'] = 'request test'
