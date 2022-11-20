from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME') # con esto defino que la variable de entorno RENDER_HOST_NAME, es igual a esa variable de entorno que defino el RENDER
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME) # si la variable de tnrono RENDER_HOST_NAME existe, entonces lo pushea a los ALLOWED_HOSTS

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default = 'sqlite:///dbsqlite3',
        # {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'elenas',
        # 'USERNAME': 'postgres',
        # 'PASSWORD': 'R4M1R0.8489',
        # 'HOST': 'localhost',
        # 'PORT': '5432'
        # },
        conn_max_age = 600
    )
    
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
if not DEBUG:
    STATIC_URL = os.path.join(BASE_DIR, 'staticFiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'