"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

__author__ = 'CyberSponse Inc-Tushar Kanade'

import json

from flask import render_template, request, redirect, url_for, jsonify
from markupsafe import escape

from app import app
from CSConfiguration import CSConfiguration
from cyops import CyOPs
from qpylib import qpylib


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

        # Escape string responses to mitigate Stored XSS
        if isinstance(result, str):
            result = escape(result)

        # If the connector already returns a dictionary, return it directly
        if isinstance(result, dict):
            return jsonify(result)

        return jsonify({
            "message": result
        })

    except Exception as err:
        qpylib.log("Error sending offense as alert: {}".format(err), "ERROR")
        return jsonify({
            "message": escape(str(err))
        }), 500
