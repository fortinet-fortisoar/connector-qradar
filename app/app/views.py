"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

__author__ = 'CyberSponse Inc-Tushar Kanade'

from flask import render_template, request, jsonify
from markupsafe import escape

from app import app
from CSConfiguration import CSConfiguration
from cyops import CyOPs
from qpylib import qpylib


def sanitize_response(data):
    """
    Recursively sanitize response data before returning JSON.
    """

    if isinstance(data, dict):
        sanitized = {}

        for key, value in data.items():
            sanitized[str(escape(str(key)))] = sanitize_response(value)

        return sanitized

    elif isinstance(data, list):
        return [sanitize_response(item) for item in data]

    elif isinstance(data, tuple):
        return tuple(sanitize_response(item) for item in data)

    elif isinstance(data, str):
        return str(escape(data))

    return data


@app.route('/cs_config', methods=['GET', 'POST'])
def admin():
    csconfig = CSConfiguration()
    csconfig.read_configuration()

    messages = []

    qpylib.log("request method: %s" % request.method)

    if request.method == 'POST':
        csconfig.get_config(request.form)
        csconfig.save_configuration()
        messages.append('Configurations have been saved.')

    csconfig.read_configuration()

    return render_template(
        'cs_config.html',
        title='Admin Screen',
        form=csconfig.config,
        messages=messages
    )


@app.route('/offense_to_cyops_alert', methods=['GET', 'POST'])
def send_offense_as_alert():
    offense_id = request.args.get('context')

    csconfig = CSConfiguration()
    csconfig.read_configuration()

    cs = CyOPs(csconfig.config)

    try:
        result = cs.send_offense_id(offense_id)

        # Sanitize complete response
        result = sanitize_response(result)

        if isinstance(result, dict):
            return jsonify(result)

        return jsonify({
            "message": result
        })

    except Exception as err:
        qpylib.log(
            "Error sending offense as alert: {}".format(err),
            "ERROR"
        )

        return jsonify(
            sanitize_response({
                "message": str(err)
            })
        ), 500