# Prod settings

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
# Get from file
SECRET_KEY = ''

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Get from file
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        # Get from file
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': ''
    }
}

# Get from file
ADMINS = ()

# # Get from file
EMAIL_HOST_USER = ''
# # Get from file
EMAIL_HOST_PASSWORD = ''

EMAIL_SUBJECT_PREFIX = '[Antyc Solutions]'