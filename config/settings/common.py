""" Contains common settings to be use in all environments.
"""

import os

from config.settings.logging_settings import LOGGING
from config.settings.socialauth_settings import *

# Path to the project directory.
PROJECT_PATH = os.path.abspath(os.curdir)

# Managers and Admins
ADMINS = (('Admin', 'mail@amythsingh.com'),)
MANAGERS = ADMINS

# Timezone, Language and other core settings
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
SECRET_KEY = '%@-bzmnxv@!8klow^pr-ughcj6rchrp(2wsg1&2++%wd^1)4xd'

# Template loaders
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
)

# Middleware classes
MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
)

# Paths and Url settings
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (os.path.join(PROJECT_PATH, 'static'),)
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

ROOT_URLCONF = 'config.urls'

# Installed apps
DJANGO_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.admin',
  'django.contrib.admindocs',
)

PROJECT_APPS = ()
THIRD_PARTY_APPS = (
    'rest_framework',
    'social_auth',
)
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# Email settings
EMAIL_HOST = 'localhost'
