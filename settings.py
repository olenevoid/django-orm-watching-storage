from dotenv import load_dotenv
from os import environ


load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': environ['HOST'],
        'PORT': environ['PORT'],
        'NAME': environ['NAME'],
        'USER': environ['USER'],
        'PASSWORD': environ['PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = environ['SECRET_KEY']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
