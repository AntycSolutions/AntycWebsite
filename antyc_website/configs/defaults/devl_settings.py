# Devl settings

from os import path

BASE_DIR = path.dirname(path.dirname(path.dirname(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
# Get from file
SECRET_KEY = ''

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Get from file
ADMINS = ()
MANAGERS = ADMINS

# Get from file
EMAIL_HOST_USER = ''
# Get from file
EMAIL_HOST_PASSWORD = ''

EMAIL_SUBJECT_PREFIX = '[Devl - Antyc] '
