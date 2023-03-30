from flask import Blueprint
from flask.views import View, MethodView


app_auth = Blueprint('app_auth', __name__)


from . import auth

from authlib.integrations.flask_oauth2 import ResourceProtector
from apps.authentication.validator import Auth0JWTBearerTokenValidator

from apps import app

AUTH0_DOMAIN = app.config['AUTH0_DOMAIN']
API_IDENTIFIER = app.config['API_IDENTIFIER']
ALGORITHMS = app.config['ALGORITHMS']

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    AUTH0_DOMAIN,
    API_IDENTIFIER
)
require_auth.register_token_validator(validator)


