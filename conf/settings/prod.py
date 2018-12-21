from .base import *

DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
MEDIA_ROOT = 'var/media'
MEDIA_URL = ''
# STATIC_ROOT =

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'var/db.sqlite3',
    }
}
