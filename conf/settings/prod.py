from .base import *

DEBUG = False
ALLOWED_HOSTS = ['poemscape.mirrors.asia', '127.0.0.1']
MEDIA_ROOT = '/var/opt/poemscape/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/opt/poemscape/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'poemscape',
        'USER': 'poemscape',
    }
}

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'poemscape@mirrors.asia'
SERVER_EMAIL = 'poemscape@mirrors.asia'
ADMINS = [('Admin', 'poemscape@0x01.me')]
