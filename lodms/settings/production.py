from .base import *

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lodms_db',
        'USER': 'lodms_user',
        'PASSWORD': 'qweqwe123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = []

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'