"""
Django settings for antyc_website project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'antyc',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'antyc_website.urls'

WSGI_APPLICATION = 'antyc_website.wsgi.application'

# Databases
DATABASES = {}

# Internationalization
LANGUAGE_CODE = 'en-ca'
TIME_ZONE = 'America/Edmonton'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
)

# Media files (user uploaded)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/media/'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

# Email
SERVER_EMAIL = 'Antyc Solutions <root@pantyc.ca>'
EMAIL_USE_TLS = True
# prod/dev
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
# dev
# run "python -m smtpd -n -c DebuggingServer localhost:1025" first
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025

if os.path.isfile(os.path.join(BASE_DIR, "../prod")):
    from .configs.prod_settings import *
elif os.path.isfile(os.path.join(BASE_DIR, "../test")):
    from .configs.test_settings import *
elif os.path.isfile(os.path.join(BASE_DIR, "../devl")):
    from .configs.devl_settings import *
else:
    raise Exception("Please create a settings decision file.")