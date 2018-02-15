"""
WSGI config for userservice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

END_OF_URL = os.environ.get("END_OF_URL", "")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "userservice.settings")

_application = get_wsgi_application()


def application(environ, start_response):
    """
    The following runs on a path of /some/random/service/
    by setting the END URL env variable (in the case of above equaling
    "service", this setup allows fo django app to run on both the above url
    and on the root url
    :param environ:
    :param start_response:
    :return:
    """
    script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
    path_test = environ['PATH_INFO'].split(END_OF_URL)
    if len(path_test) > 1:
        environ['SCRIPT_NAME'] = path_test[0] + END_OF_URL
        if environ['PATH_INFO'].startswith(script_name):
            environ['PATH_INFO'] = path_test[1]
    return _application(environ, start_response)
