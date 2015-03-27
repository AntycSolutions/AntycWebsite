"""
WSGI config for antyc project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "antyc.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
