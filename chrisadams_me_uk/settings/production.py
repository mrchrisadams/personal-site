from __future__ import absolute_import, unicode_literals

import os

# Parse database configuration from $DATABASE_URL
import dj_database_url

from .base import *

# Pull the secret key out of an environment variable to keep it out of source control
env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']


DATABASES['default'] = dj_database_url.config()

DJANGO_SETTINGS_MODULE=chrisadams_me_uk.settings.production
SECRET_KEY='####' #Replace this with your own randomly generated, 50 character key

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
