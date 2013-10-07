from os.path import abspath, dirname, join
import sys

PROJECT_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(join(PROJECT_PATH, 'apps'))

PUBLIC_PATH = join(PROJECT_PATH, 'public')

DEBUG = False
TEMPLATE_DEBUG = True

ADMINS = (
    # ('', ''),
)

MANAGERS = ADMINS

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = join(PUBLIC_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = join(PUBLIC_PATH, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    join(PROJECT_PATH, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.views.decorators.csrf._EnsureCsrfCookie',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'allmywishes.urls'

WSGI_APPLICATION = 'allmywishes.wsgi.application'

TEMPLATE_DIRS = (
    join(PROJECT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

FIXTURE_DIRS = (
    join(PROJECT_PATH, 'fixtures'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Plugins:
    'south',
    'rest_framework',
    'sorl.thumbnail',

    # Apps:
    'core',
    'accounts',
    'wish',
)

APPEND_SLASH = False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join(PROJECT_PATH, 'logs', 'allmywishes.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 50,
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    'DEFAULT_RENDERER_CLASSES': (
        'core.renderers.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'core.parsers.CamelCaseJSONRenderer',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
}

AUTHENTICATION_BACKENDS = (
    'accounts.backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'accounts.Account'

REDABILITY = {
    "API_TOKEN": "dc16f836beb32cb92551b866ee683538dd2c4a4b",
    "API_STARTPOINT": "http://www.readability.com/",
    "API_PARSE_URL": "/api/content/v1/parser",
}

EMBEDLY = {
    "API_KEY": "5c56637d4cd94a5281bbdb08c9ed86b4",
    "API_URL": "https://api.embed.ly/1/oembed"
}
