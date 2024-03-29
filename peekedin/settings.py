# Django settings for peekedin project.

import dj_database_url
import os

print("Running peekedin/settings")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Abe', 'abe.music@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'd2kcbm4o5gjg1d',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'tjntohrdpwuzct',
        'PASSWORD': 'c2SpK9flZWvNFMo7l5D73rymjw',
        'HOST': 'ec2-54-235-155-40.compute-1.amazonaws.com',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

# DB provided by Heroku <3
# DATABASES['default'] = dj_database_url.config(default='postgres://peekedin:password@localhost:5432/peekedin')
# DATABASES['default'] =  dj_database_url.config()

# From Heroku getting started guide. Not sure? Sounds important.
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, '..', 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '5y10!cxjkvb@(o48j=&5wl539=#4%pj3*+#rc%ml55k^-c1fyz'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'peekedin.middleware.disable_csrf',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'peekedin.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'peekedin.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'rest_framework',
    'dashboard',
    'core',
    'leads',
)

# Extended user profile
AUTH_PROFILE_MODULE= 'core.UserProfile'

LINKEDIN_TOKEN = '8bd33660-2174-4381-89df-9bd8e2b0aac0'
LINKEDIN_SECRET = '5586ae55-478c-4b38-851d-0f53b10110c1'

SNITCH_SERVICE_URL = 'http://precruit-api.yuna.codemeu.com/api/v1/fetch_lead/AQW04SSowQGitG_JwyZxqZV5g_SYUk9b4DIsQ0K7EJzYTy8KNsqapEsQjJ7ZZ4X1LlrVaJQt4D3CkKNYS9mwxxQP4cUF2m1t9BTR2OFFos1ANUz2lCDx-BaQ9vqXl1lJWY7gT6BeMGZ80BxrSd1s2DaUzHCnUtYBErLSdH5UVA81KMx05Ek?url='

# Django Rest Framework configuration
REST_FRAMEWORK = {
    #'DEFAULT_AUTHENTICATION_CLASSES': (
    #    #'core.authentication.BaseAuthentication',
    #    'rest_framework.authentication.SessionAuthentication',
    #),
    'PAGINATE_BY': 10,
    'PAGINATE_BY_PARAM': 'page_size'
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)s [%(levelname)s]:%(message)s',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            #'handlers': ['mail_admins'],
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'peekedin': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'dashboard': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'peekedin.dashboard': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
