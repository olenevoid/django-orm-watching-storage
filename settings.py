from dotenv import load_dotenv
from os import environ

load_dotenv()

HOST = environ['HOST']
PORT = environ['PORT']
NAME = environ['NAME']
USER = environ['USER']
PASSWORD = environ['PASSWORD']

SECRET_KEY_VALUE = environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = SECRET_KEY_VALUE

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
