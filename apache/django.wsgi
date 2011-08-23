import os, sys

#path = '/home/daniel/projects/fanfar-folizz/festival/'
#if path not in sys.path:
#    sys.path.append(path)

#os.environ['DJANGO_SETTINGS_MODULE'] = 'festival.settings'


_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _PROJECT_DIR)
sys.path.insert(0, os.path.dirname(_PROJECT_DIR))

_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]
os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
