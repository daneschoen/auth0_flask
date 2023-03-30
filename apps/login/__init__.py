from flask import Blueprint
from flask.views import View, MethodView


app_login = Blueprint('app_login', __name__, template_folder='templates')


from authlib.integrations.flask_client import OAuth

from apps import app

oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=app.config["AUTH0_CLIENT_ID"],
    client_secret=app.config["AUTH0_CLIENT_SECRET"],
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{app.config["AUTH0_DOMAIN"]}/.well-known/openid-configuration'
)


from . import views_login




