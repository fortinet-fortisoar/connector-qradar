"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

__author__ = 'CyberSponse Inc-Tushar Kanade'

import json
import os

from markupsafe import escape
from qpylib import qpylib


class CSConfiguration(object):
    filename = os.path.join(
        qpylib.get_store_path(),
        'cs_config.json'
    )

    def __init__(self):
        """Initial Config"""
        self.config = {
            'cyops_url': '',
            'username': '',
            'password': '',
        }

    @staticmethod
    def _sanitize_string(value):
        """
        Validate and sanitize string values.
        """
        if value is None:
            return ""

        if not isinstance(value, str):
            value = str(value)

        return str(escape(value.strip()))

    def read_configuration(self):
        qpylib.log('reading configuration: ' + self.filename)

        if not os.path.isfile(self.filename):
            qpylib.log('could not find config file. Use default values')
            return

        with open(self.filename, 'r', encoding='utf-8') as data:
            config = json.load(data)

        # Only allow expected configuration keys
        self.config = {
            'cyops_url': self._sanitize_string(
                config.get('cyops_url', '')
            ),
            'username': self._sanitize_string(
                config.get('username', '')
            ),
            'password': self._sanitize_string(
                config.get('password', '')
            )
        }

    def save_configuration(self):
        with open(self.filename, 'w', encoding='utf-8') as data:
            json.dump(self.config, data)

        qpylib.log('saved new configuration')

    def get_config(self, form):
        for key, value in form.iteritems():
            qpylib.log('key: %s, value: %s' % (key, value))

            if key not in self.config:
                continue

            if len(str(value).strip()):
                self.config[key] = self._sanitize_string(value)
