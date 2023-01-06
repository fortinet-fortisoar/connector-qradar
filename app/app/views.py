__author__ = 'CyberSponse Inc-Tushar Kanade'

import json
from flask import render_template, request, redirect, url_for
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
    return render_template('cs_config.html', title='Admin Screen', form=csconfig.config, messages=messages)


@app.route('/offense_to_cyops_alert', methods=['GET', 'POST'])
def send_offense_as_alert():
    offense_id = request.args.get('context')
    csconfig = CSConfiguration()
    csconfig.read_configuration()
    cs = CyOPs(csconfig.config)
    return json.dumps({'message': cs.send_offense_id(offense_id)})