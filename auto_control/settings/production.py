from .base import *

DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql_db',
        'PORT': '3306',
        'PASSWORD': 'or/Hw0fPnYTtYGQ15YZ/rhNDBv6WiciT',
        'USER': 'root',
        'HOST': '127.0.0.1',
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

