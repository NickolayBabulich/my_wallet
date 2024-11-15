from .base import *

# INSTALLED_APPS += ['',]

INTERNAL_IPS = ['127.0.0.1']

# AUTH_USER_MODEL = 'accounts.User'

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
