from .base import *

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = False

# INTERNAL_IPS = ['127.0.0.1',]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/lodms_local2.sqlite3'),
    }
}


MIDDLEWARE += [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
]
