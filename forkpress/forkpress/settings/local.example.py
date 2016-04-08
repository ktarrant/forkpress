from .base import *
from os.path import join

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ("127.0.0.1", )
