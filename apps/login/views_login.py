import json
from urllib.parse import quote_plus, urlencode
from flask import Flask, redirect, render_template, session, url_for, jsonify
from auth0.authentication import Database

from apps import app
from . import app_login
from . import oauth


AUTH0_DOMAIN = app.config["AUTH0_DOMAIN"]
AUTH0_CLIENT_ID = app.config["AUTH0_CLIENT_ID"]


@app_login.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("app_login.callback", _external=True)
    )

@app_login.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("")


# @app.route('/logout')
# @auth0.requires_auth
# def logout():
#    auth0.logout()
#    return jsonify('logout')

@app_login.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + AUTH0_DOMAIN
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("app_login.home", _external=True),
                "client_id": AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        )
    )


@app_login.route("/")
def home():
    return render_template("index.html", 
                           session=session.get('user'), 
                           pretty=json.dumps(session.get('user'), indent=4))

