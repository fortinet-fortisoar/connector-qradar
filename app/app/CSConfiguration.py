__author__ = 'CyberSponse Inc-Tushar Kanade'

import json
import os
import copy

from qpylib import qpylib


class CSConfiguration(object):
    filename = os.path.join(qpylib.get_store_path(),
                            'cs_config.json')

    def __init__(self):
        """ Initial Config """
        self.config = {
            'cyops_url': '',
            'username': '',
            'password': '',
        }

    def read_configuration(self):
        qpylib.log('reading configuration: ' + self.filename)
        if not os.path.isfile(self.filename):
            # Just use default values
            qpylib.log('could not find config file. Use default values')
            return
        with open(self.filename, 'rb') as data:
            self.config = json.load(data)

    def save_configuration(self):
        with open(self.filename, 'wb') as data:
            json.dump(self.config, data)
        qpylib.log('saved new configuration')

    def get_config(self, form):
        for key, value in form.iteritems():
            qpylib.log('key: %s, value: %s' % (key, value))
            if len(str(form[key]).strip()):
                self.config[key] = form[key]
