from .base import *

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lodms',
        'USER': 'mamun',
        'PASSWORD': 'qweqwe123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# STATICFILES_DIRS += [
	
# ]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'