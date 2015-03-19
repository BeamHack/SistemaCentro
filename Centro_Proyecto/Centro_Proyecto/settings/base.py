from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)
SECRET_KEY = '3z45mp17#=gsst!9dqi#bdw7wu!w-0m1@$reipvh%l&(xk0g2k'

DJANGO_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] 

THIRD_PARTY_APPS=[
    
]

LOCAL_APPS=[
    'apps.home',
    'apps.usuario',
    'apps.seguro',
    'apps.paciente',
    'apps.medicacion',
    'apps.receta',
    'bootstrapform',
]

INSTALLED_APPS = DJANGO_APPS+THIRD_PARTY_APPS+LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MEDIA_ROOT = '/home/fernando/Escritorio/'

MEDIA_URL = '/media/'


ROOT_URLCONF = 'Centro_Proyecto.urls'

WSGI_APPLICATION = 'Centro_Proyecto.wsgi.application'


LANGUAGE_CODE = 'es-ecu'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS=[BASE_DIR.child("templates")]

AUTHENTICATION_BACKENDS=(
    'apps.usuario.backends.EmailBackend',

)