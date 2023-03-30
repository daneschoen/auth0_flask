from flask import Blueprint
from flask.views import View, MethodView


app_test = Blueprint('app_test', __name__, template_folder='templates')


from . import views_test
