from dotenv import load_dotenv
from os import environ


load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': environ['DB_HOST'],
        'PORT': environ['DB_PORT'],
        'NAME': environ['DB_NAME'],
        'USER': environ['DB_USER'],
        'PASSWORD': environ['DB_PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = environ['SECRET_KEY']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
