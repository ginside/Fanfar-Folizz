"""
WSGI config for testort project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "festival.settings")

from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()

def application(environ, start_response):
    if 'FANFAR_BASE_URL' in os.environ.keys():
        os.environ['FANFAR_BASE_URL'] = environ['FANFAR_BASE_URL']
        return _application(environ, start_response)
