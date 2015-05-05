from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ''

DEBUG = True
THUMBNAIL_DEBUG = DEBUG

# COMPRESS_ENABLED = True

# ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += (
    # 'django-debug-toolbar',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'HOST': 'localhost',
        'USER': '',
        'PASSWORD': '',
        'PORT': ''
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your-username@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }


COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    # ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
    # ('text/x-scss', 'sass --style compressed {infile} {outfile}'),
)
