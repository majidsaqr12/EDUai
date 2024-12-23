from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-5qc0wnqq_hrq7w5wq^5*()8jp(=@!t+c5sg=nx#hhck+78zh0e'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

CORS_ALLOW_ALL_ORIGINS = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django.contrib.sitemaps',
    'pages',
    'accounts',
    'subjects',
    "corsheaders",
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
    'django_otp.middleware.OTPMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'eduai.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eduai.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Set the default language to French
LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'
USE_TZ = True

# Enable localization and translation
USE_I18N = True
USE_L10N = True

# List of available languages
LANGUAGES = [
    ('fr', 'Français'),
    ('en', 'English'),
    ('ar', 'Arabic')
]

# Define where the translations will be stored
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


STATIC_URL = 'static/'
MEDIA_URL = '/media/'

# if DEBUG:
#     STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'eduai/static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'majidsakr86@gmail.com'
EMAIL_HOST_PASSWORD = 'woyw ilce nibj ufde'
ADMIN_EMAIL = 'majidsakr86@gmail.com'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
