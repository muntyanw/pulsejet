import os
from pathlib import Path

# BASE_DIR – корневая директория, где находится manage.py
BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

SECRET_KEY = 'ваш-секретный-ключ'
DEBUG = True

#ALLOWED_HOSTS = ['pulsejet.vello-doro.eu', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pulsejet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Можно задать общий каталог шаблонов:
        'DIRS': [BASE_DIR / 'portal' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # для доступа к request в шаблонах
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portal.context_processors.texts_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'pulsejet.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pulsejet_db',
        'USER': 'pulsejet_user',
        'PASSWORD': '88888888',
        'HOST': 'localhost',
        'PORT': '',
    }
}


LANGUAGE_CODE = 'uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
USE_L10N = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# URL, на который перенаправляется пользователь после входа/выхода
LOGIN_REDIRECT_URL = '/account/'
LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/accounts/login/'

LANGUAGES = [
    ('uk', 'Українська'),
    ('en', 'English'),
    
    #('ru', 'Русский'),
]


AUTH_USER_MODEL = 'portal.CustomUser'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_AGE = 1209600  # 2 недели

