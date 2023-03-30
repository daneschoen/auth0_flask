from flask import render_template, request, redirect, url_for, g, \
    abort, session, flash, logging, make_response, Response, jsonify

from apps import app
from . import app_test


@app_test.route('test')
def run_tests():
    return jsonify({'sanity': 'ok'})
