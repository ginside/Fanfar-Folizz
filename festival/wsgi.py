"""
WSGI config for testort project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "festival.settings")

import django.core.handlers.wsgi
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    os.environ['FANFAR_BASE_URL'] = environ['FANFAR_BASE_URL']
    return _application(environ, start_response)
