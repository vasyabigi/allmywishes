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
        'NAME': get_env_variable("ALLMYWISHES_DATABASE_NAME_DEV"),
        'USER': get_env_variable("ALLMYWISHES_DATABASE_USER"),
        'PASSWORD': get_env_variable("ALLMYWISHES_DATABASE_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECRET_KEY = get_env_variable("ALLMYWISHES_SECRET_KEY")

EMBEDLY_API_KEY = get_env_variable("ALLMYWISHES_EMBEDLY_API_KEY")

RAVEN_CONFIG = {
    'dsn': 'http://de22fa73ed0c4d17b4e5b379f6949672:006dd405fc37472eacd8ba5de7f1645e@sentry.vasyabigi.com/5',
}

INSTALLED_APPS += (
    "gunicorn",
    'raven.contrib.django.raven_compat'
)

ALLOWED_HOSTS = ['dev.allmywish.es']
