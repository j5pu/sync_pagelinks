"""
Django settings for sync_pagelinks project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qv5n8j%y@3n&c#_#@9fm-+-q03_02j_(x9&lg4@j!2v$!d#5e7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'phasionate',
    'igoo_co',
    'twitter_bots_prod',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sync_pagelinks.urls'

WSGI_APPLICATION = 'sync_pagelinks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sync_pagelinks',
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
    },
    'phasionate': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'phasionate',
        "USER": "bizeulabswpuser",
        "PASSWORD": "1aragon1",
        "HOST": "104.236.21.5",
    },
    'igoo_co': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'redirection',
        "USER": "root",
        "PASSWORD": "1aragon1",
        "HOST": "igoo.co",
    },
    'twitter_bots_prod': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'twitter_bots_prod',
        "USER": "root",
        "PASSWORD": "1aragon1",
        "HOST": "192.168.1.115",
    },
}

DATABASE_ROUTERS = ('phasionate.phasionate_router.PhasionateRouter',
                    'igoo_co.igoo_co_router.IgooCoRouter',
                    'twitter_bots_prod.twitter_bots_router.TwitterBotsRouter',)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            # 'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            'format': "[%(asctime)s] [%(name)s:%(lineno)s] %(threadName)s - %(levelname)s  %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        # 'null': {
        #     'level':'DEBUG',
        #     'class':'django.utils.log.NullHandler',
        # },
        'console_info': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stdout
        },
        'console_error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'db_log_file':{
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/db_querys.log'),
            'maxBytes': '16777216', # 16megabytes
            'formatter': 'verbose'
        },
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'filters': ['require_debug_false'],
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     'include_html': True,
        # }
    },
    'loggers': {
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': True,
        # },
        'core.management.commands': { # I keep all my of apps under 'apps' folder, but you can also add them one by one, and this depends on how your virtualenv/paths are set
            'handlers': ['console_info', 'console_error'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['db_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    # # you can also shortcut 'loggers' and just configure logging for EVERYTHING at once
    # 'root': {
    #     'handlers': ['console', 'mail_admins'],
    #     'level': 'INFO'
    # },
}