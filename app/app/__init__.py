"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

__author__ = 'IBM'

import os
import os.path
import sys
import json
import re

from flask import Flask
from flask import send_from_directory, render_template, request, abort
from werkzeug.utils import safe_join

from qpylib import qpylib

app = Flask(__name__)

# Create log here to prevent race condition when importing views
qpylib.create_log()

qpylib.register_jsonld_endpoints()

from app import views


@app.route('/debug')
def debug():
    return send_from_directory('/store/log/', 'app.log')


@app.route('/debug_view')
def debug_view():
    """
    Display the debug log.
    Jinja2 escapes variables by default, preventing XSS.
    """
    try:
        with open(
            '/store/log/app.log',
            'r',
            encoding='utf-8',
            errors='replace'
        ) as log_file:
            debug_content = log_file.read()

        return render_template(
            'debug.html',
            debug_content=debug_content
        )

    except Exception as err:
        qpylib.log(
            "Unable to read debug log: {}".format(err),
            "ERROR"
        )
        abort(500)


@app.route('/resources/<path:filename>')
def send_file(filename):
    """
    Securely serve static resources.
    """

    resources_dir = os.path.join(app.static_folder, 'resources')

    # Normalize path
    filename = os.path.normpath(filename)

    # Reject traversal attempts
    if filename.startswith("..") or os.path.isabs(filename):
        abort(404)

    # Allow only expected file extensions
    allowed_extensions = {
        ".css",
        ".js",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".ico",
        ".woff",
        ".woff2",
        ".ttf",
        ".eot",
        ".map"
    }

    extension = os.path.splitext(filename)[1].lower()

    if extension not in allowed_extensions:
        abort(404)

    # Build secure path
    safe_path = safe_join(resources_dir, filename)

    if safe_path is None:
        abort(404)

    if not os.path.isfile(safe_path):
        abort(404)

    # Use validated relative filename
    safe_filename = os.path.relpath(safe_path, resources_dir)

    qpylib.log(">>> route resources >>>")
    qpylib.log("resource={}".format(safe_filename))

    return send_from_directory(
        resources_dir,
        safe_filename,
        conditional=True
    )


@app.route('/log_level', methods=['POST'])
def log_level():
    """
    Update application log level.
    """

    level = request.form.get('level', '').upper()

    supported_levels = {
        'INFO',
        'DEBUG',
        'ERROR',
        'WARNING',
        'CRITICAL'
    }

    if level not in supported_levels:
        return (
            "Unsupported log level. Supported values: {}".format(
                ", ".join(sorted(supported_levels))
            ),
            400
        )

    qpylib.set_log_level(level)

    return "Log level successfully updated."


@app.route('/react-intl/<path:requested>', methods=['GET'])
def reactIntl(requested):

    def put_in_container(container, key, value):
        key_parts = key.split(".")

        s = len(key_parts)
        l = 0

        while s > 1:
            part = key_parts[l]

            if part not in container:
                container[part] = {}

            container = container[part]
            s -= 1
            l += 1

        container[key_parts[l]] = value

    resources = os.path.dirname(
        os.path.abspath(sys.argv[0])
    ) + "/app/static/resources"

    requested_language = None
    requested_locale = None

    lang_locale = re.compile("[_\\-]").split(requested)

    if len(lang_locale) == 2:
        requested_language = lang_locale[0]
        requested_locale = lang_locale[1]
    else:
        requested_language = requested
        requested_locale = None

    qpylib.log(
        "Requested language {0}, locale {1}".format(
            requested_language,
            requested_locale
        ),
        "DEBUG"
    )

    result = {
        "locales": [],
        "messages": {}
    }

    for f in os.listdir(resources):

        bundle_lang = f.split("_")

        locale = None

        if len(bundle_lang) == 2:
            language = bundle_lang[1].split(".")[0]
        else:
            language = bundle_lang[1]
            locale = bundle_lang[2].split(".")[0]

        qpylib.log(
            "Bundle {0} language {1}, locale {2}".format(
                f,
                language,
                locale
            ),
            "DEBUG"
        )

        if language == requested_language:

            filepath = os.path.join(resources, f)

            if os.path.isfile(filepath):

                with open(filepath) as thefile:

                    lang = {}

                    for line in thefile:

                        line = line.strip()

                        if len(line) > 0:

                            key_value = line.split("=")

                            put_in_container(
                                lang,
                                key_value[0].strip(),
                                key_value[1].decode('unicode-escape')
                            )

                    if locale is None:
                        result["locales"].append(language)
                    else:
                        result["locales"].append(
                            language + "_" + locale
                        )

                    result["messages"].update(lang)

    return json.dumps(result)


# Register the new q_url_for() method for use with Jinja2 templates
app.add_template_global(qpylib.q_url_for, 'q_url_for')