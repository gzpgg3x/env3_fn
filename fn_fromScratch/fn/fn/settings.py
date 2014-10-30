"""
Django settings for fn project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from mezzanine.project_template.settings import *
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mz0@g5cnbdr(@idoj(=itcw-mkt)v&2h%oeufkao0u78*)%at-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# INSTALLED_APPS = (
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# )

INSTALLED_APPS = (
    "fn.main", # the main app
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.accounts",

    # gunicorn for production
    # gunicorn_django --daemon -b 127.0.0.1:17734 -w 2 --max-requests 500
    "gunicorn",

    # =persona for authentication
    "django_browserid",
    
    # south for migrations
    # "south",
)

# from /fn-env/src/mezzanine/mezzanine/project_template
AUTHENTICATION_BACKENDS = (
    "mezzanine.core.auth_backends.MezzanineBackend",
    "django_browserid.auth.BrowserIDBackend", # =persona
)

ACCOUNTS_PROFILE_FORM_EXCLUDE_FIELDS = (
    "email",
    "first_name",
    "last_name",
)

# from /fn-env/src/mezzanine/mezzanine/project_template
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    # "mezzanine.conf.context_processors.settings",    
    "mezzanine.conf.context_processors.settings",
    #"django_browserid.context_processors.browserid", # =persona
)

LOGIN_REDIRECT_URL = '/' # =persona
LOGIN_REDIRECT_URL_FAILURE = '/' # =persona
LOGOUT_REDIRECT_URL = '/' # =persona

# remove?
MIDDLEWARE_CLASSES = (["mezzanine.core.middleware.UpdateCacheMiddleware"] +
                      list(MIDDLEWARE_CLASSES) +
                      ["mezzanine.core.middleware.FetchFromCacheMiddleware"])
MIDDLEWARE_CLASSES.remove("mezzanine.pages.middleware.PageMiddleware")

# Mezzanine
AUTH_PROFILE_MODULE = "main.Profile"
SITE_TITLE = "Food News"
RATINGS_RANGE = (-1, 1)
RATINGS_ACCOUNT_REQUIRED = True
COMMENTS_ACCOUNT_REQUIRED = True
ACCOUNTS_PROFILE_VIEWS_ENABLED = True

# Drum
ALLOWED_DUPLICATE_LINK_HOURS = 24 * 7 * 3
ITEMS_PER_PAGE = 30

try:
    from local_settings import *
except ImportError:
    pass

try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())




# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )

ROOT_URLCONF = 'fn.urls'

WSGI_APPLICATION = 'fn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
