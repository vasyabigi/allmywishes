import os
from django.core.exceptions import ImproperlyConfigured

from .common import *


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)


DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': get_env_variable("ALLMYWISHES_DATABASE_NAME"),
        'USER': get_env_variable("ALLMYWISHES_DATABASE_USER"),
        'PASSWORD': get_env_variable("ALLMYWISHES_DATABASE_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECRET_KEY = get_env_variable("ALLMYWISHES_SECRET_KEY")

EMBEDLY_API_KEY = get_env_variable("ALLMYWISHES_EMBEDLY_API_KEY")

RAVEN_CONFIG = {
    'dsn': 'http://2835370261294552a47644f67493a884:562d44e635af4ff5aee0cda093437277@sentry.vasyabigi.com/4',
}

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
    "gunicorn",
)

ALLOWED_HOSTS = ['allmywish.es']
