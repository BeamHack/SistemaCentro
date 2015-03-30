from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CentroDialisis',
        'USER':'fernando',
        'PASSWORD':'mantenimiento',
        'HOST':'localhost',
        'PORT':'5432',
    }
}
STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS=[BASE_DIR.child('static')]