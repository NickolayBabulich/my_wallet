from .base import *

INSTALLED_APPS += ['apps.account.apps.AccountConfig', ]

INTERNAL_IPS = ['127.0.0.1']

AUTH_USER_MODEL = 'account.User'

ADMIN_EMAIL = env('ADMIN_EMAIL')
ADMIN_PASSWORD = env('ADMIN_PASSWORD')

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

timezone = 'UTC'
task_serializer = 'json'
accept_content = ['json']
result_serializer = 'json'
broker_url = 'amqp://guest:guest@localhost:5672//'
task_always_eager = False
task_store_eager_result = True
broker_connection_retry_on_startup = True

PASSWORD_RESET_TIMEOUT = timedelta(minutes=env('PASSWORD_RESET_TIMEOUT', default=15)).total_seconds()
