"""
Django development settings for auto_control project.

Generated by 'django-admin startproject' using Django 3.2.15.
"""

from .base import *

DEBUG = True

# Development-specific apps
INSTALLED_APPS += ['debug_toolbar', ]

# Development-specific middleware
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# Local SQLite database for development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql_db',
        'PORT': '3306',
        'PASSWORD': '12345678',
        'USER': 'root',
        'HOST': '127.0.0.1',
    }
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:4200',  # Allow the Angular app to make requests
]