from .production import *

import django_heroku
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dchak7tu6s0dvi',
        'USER': 'gvpxiianontmyr',
        'PASSWORD': 'bc71beb71258505d9e6deaa5830ad0eb59df835b047dcbff6162f523d6ecf26e',
        'HOST': 'ec2-23-23-180-121.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# django_heroku.settings(locals())