"""
Django settings for shop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iv2olpytkx=qr_%9asqe+u)rs*)%sqbo3vrz&n=&2gwqt2qn^l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ADMINS = (
('Maxymeko Andrij', 'amax9x@gmail.com'),
)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1:8000',
    '.example.com',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    'profile.context_processor.context_profile',
)


TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'banner',
    'product',
    'cart',
    'profile',
    'booking',
    'contact',
    'about',
    'delivery',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'shop.urls'

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_BANNER_TITLE = 3
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#MEDIA_ROOT = 'home/andrey/Projects/printershop/Django-ComPlex/shop/media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
#ADMIN_MEDIA_PREFIX = '/media/admin/'
#MEDIA_ROOT = '/home/ukrainem/domains/ukrainemotors.com/public_html/media/'
#STATIC_ROOT = '/home/ukrainem/domains/ukrainemotors.com/public_html/static/'
STATICFILES_DIRS = (
os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)