"""
Django settings for PFA project.

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
SECRET_KEY = 'w(mtu#%%2h#c*dnqs%8k#zw)sye_qi7wdsegekke(vsu(^7@)s'

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
    # add here your apps
    'phiauth',
    'cms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'PFA.urls'

WSGI_APPLICATION = 'PFA.wsgi.application'

ADMINS = (
    ('Thomas Miele', 'thomas.miele@epitech.eu'),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'PFA/dbs/db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR

STATICFILES_DIRS = (
    'PFA/static',
)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR + '/PFA/dbs/media/'

# Apps templates dir tree
# always make subdir templates
# in subdir "templates" -> make subdir with appname
# So for use a template files, you do "AppName/file.html"
# If you want to use a template file from another app
# you can do use "AnotherAppName/same_name_template.html"
# |--appname
#    |-- templates
#        |-- appname
#            *.html
TEMPLATE_DIRS = (
    # syntax : appname/templates
    # project dir
    'PFA/templates',
    # here, add apps templates
    'auth/templates',
    'cms/templates',
)

LOGIN_URL = '/auth/login/'
