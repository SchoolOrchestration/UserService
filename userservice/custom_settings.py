from .helper import get_secret
import os


VERSION = '1'

if os.environ.get('SENTRY_PROJECT_NUMBER', None):
    RAVEN_CONFIG = {
        'dsn': 'https://%s@sentry.io/%s' % (
            get_secret("USERSERVICE_SENTRY_TOKEN"),
            get_secret("SENTRY_PROJECT_NUMBER")
        )
    }

REST_FRAMEWORK = {
    # Parser classes priority-wise for Swagger
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
}

ALLOWED_HOSTS = ["*"]

AWS_STORAGE_BUCKET_NAME = 'static-api-vumatel-coza'
AWS_AUTO_CREATE_BUCKET = True
AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = 'eu-central-1'

# AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
STATIC_URL = "https://s3.amazonaws.com/{}/".format(AWS_STORAGE_BUCKET_NAME)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DATABASE_NAME', 'postgres'),
        'USER': get_secret('DATABASE_USER', 'postgres'),
        'HOST': get_secret('DATABASE_HOST', 'db'),
        'PORT': get_secret('POSTGRES_DB_PORT', '5432'),
    }
}

db_password = get_secret('USERSERVICE_DATABASE_PASSWORD', False)
if db_password:
    DATABASES.get('default').update({'PASSWORD': db_password})

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'APIS_SORTER': 'alpha',
    'OPERATIONS_SORTER': 'method',
    'JSON_EDITOR': True,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'patch'
    ],
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    }
}
