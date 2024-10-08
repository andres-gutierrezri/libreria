"""
Django settings for EVA project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Importar os para manejar las variables de entorno
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from dotenv import load_dotenv
from EVA.local_settings import IS_DEPLOYED, DATABASE_DICT
from EVA.logging_settings import *
from EVA.cloud_settings import *

# Carga las variables de entorno del archivo .env
load_dotenv()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@arios-ing.com'
EMAIL_HOST_PASSWORD = 'aympwbumzwbibbyh'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = f'"EVA" <{EMAIL_HOST_USER}>'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a1e+7^&ozbdlfhmkdmg@ic9-%*brp1khg%b_#1v-bksm#=-ehw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not IS_DEPLOYED

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', 'arios-eva.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['http://*', 'https://arios-eva.up.railway.app']    

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'whitenoise.runserver_nostatic',
    'storages',
    'Administracion.apps.AdministracionConfig',
    'Proyectos.apps.ProyectosConfig',
    'TalentoHumano.apps.TalentohumanoConfig',
    'Financiero.apps.FinancieroConfig',
    'SGI.apps.SgiConfig',
    'Notificaciones.apps.NotificacionesConfig',
    'GestionDocumental.apps.GestiondocumentalConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'EVA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'EVA/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'eva_tags': 'EVA.templatetags.etiquetas_generales',
            }
        },
    },
]

WSGI_APPLICATION = 'EVA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': DATABASE_DICT
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/staticfiles/' if IS_DEPLOYED else '/static/'

"""
# Configuración para almacenar archivos estáticos en S3
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
"""

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'EVA/static'),
    os.path.join(BASE_DIR, 'Administracion', 'static', 'Administracion'),
    os.path.join(BASE_DIR, 'Proyectos', 'static', 'Proyectos'),
    os.path.join(BASE_DIR, 'TalentoHumano', 'static', 'TalentoHumano'),
    os.path.join(BASE_DIR, 'Financiero', 'static', 'Financiero'),
    os.path.join(BASE_DIR, 'SGI', 'static', 'SGI'),
    os.path.join(BASE_DIR, 'Notificaciones', 'static', 'Notificaciones'),
    os.path.join(BASE_DIR, 'GestionDocumental', 'static', 'GestionDocumental'),
)

# Configuración para almacenar archivos multimedia en el sistema de archivos (S3)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if not IS_DEPLOYED:
    MEDIA_URL = '/media/'
else:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

# Son 10800 segundos equivalentes a 3 horas.
SESSION_COOKIE_AGE = 10800

EVA_PUBLIC_MEDIA = 'publico'
EVA_PRIVATE_MEDIA = 'privado'

# Por defecto se dejan las ip para el entorno de desarrollo.
EVA_ACCESO_EXTERNO = os.environ.get('eva_acceso_externo', '127.0.0.1:8000')
EVA_ACCESO_INTERNO = os.environ.get('eva_acceso_interno', '127.0.0.1:8000')

EVA_RUTA_ARCHIVOS_FACTURA = os.environ.get('eva_ruta_archivos_factura', 'C:/AJAR/facelec/')
EVA_URL_BASE_FACELEC = os.environ.get('eva_url_base_facelec', 'http://localhost:8080/api/facturacion/')

JASPERSERVER_URL = os.environ.get('jasperserver_url', 'http://localhost:8081/jasperserver/rest_v2/reports/EVA/')
JASPERSERVER_USUARIO = os.environ.get('jasperserver_usuario', 'jasperadmin')
JASPERSERVER_CLAVE = os.environ.get('jasperserver_clave', 'jasperadmin')

EVA_RECAPTCHA_SITE_KEY = os.environ.get('eva_recaptcha_site_key', '6Ld5nDgaAAAAAEMfhGZpUy48mKaGvowqVJyOulqI')
EVA_RECAPTCHA_SECRET_KEY = os.environ.get('eva_recaptcha_secret_key', '6Ld5nDgaAAAAAJf0aZ4axs6ocqqk6SXk5bQk7tLH')

EVA_RUTA_ARCHIVOS_TEMPORALES = os.environ.get('eva_ruta_archivos_temporales', os.path.join(MEDIA_ROOT, EVA_PRIVATE_MEDIA, 'Temp'))
