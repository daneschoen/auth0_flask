import json

from flask import Flask, request, jsonify, _request_ctx_stack, Response
from flask_cors import cross_origin

from apps.authentication.auth import requires_auth, requires_scope, AuthError
from apps.authentication import require_auth
from . import app_api


# Controllers API
@app_api.route("public")
@cross_origin(headers=["Content-Type", "Authorization"])
def public():
    response = "From a public endpoint - no authentication"
    return jsonify(message=response)


@app_api.route("private")
@cross_origin(headers=["Content-Type", "Authorization"])
@cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:3000"])
@requires_auth
def private():
    response = "from a private endpoint! You need to be authenticated to see this."
    return jsonify(message=response)

@app_api.route("private2")
@require_auth(None)
def private2():
    response = (
        "from a private endpoint 2 - You need to be"
        " authenticated to see this."
    )
    return jsonify(message=response)


@app_api.route("private-scoped")
@cross_origin(headers=["Content-Type", "Authorization"])
@cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:3000"])
@requires_auth
def private_scoped():
    if requires_scope("read:messages"):
        response = "from a private endpoint! You need to be authenticated and have a scope of read:messages to see this."
        return jsonify(message=response)
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource"
    }, 403)


@app_api.route("private-scoped2")
@require_auth("read:messages")
def private_scoped2():
    response = (
        "private scoped endpoint - You need to be"
        " authenticated and have a scope of read:messages"
    )
    return jsonify(message=response)

