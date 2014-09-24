""" Settings to be used in development environment.
"""

from config.settings.common import *

# Debug settings.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database Settings
DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'devdb',
      'USER': 'root',
      'PASSWORD': 'Puresy307',
      'HOST': '',
      'PORT': '',
  }
}

