from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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