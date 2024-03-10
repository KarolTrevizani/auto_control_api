from .base import *

DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        # In production we will use MySQL
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

