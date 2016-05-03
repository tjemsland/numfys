from .base import *
import os

# SECURITY WARNING: Do NOT run in debug mode on the production server.
DEBUG = True

# SECURITY WARNING: You have to generate a new secret key when setting up the production server.
# Keep it secret.
SECRET_KEY = 'zek$#1$0@(i$t5(q*ne-r$s29#yhe9)!g$y9vc_-th4*0dxfi4'

# Use a more lightweight database than MySQL when developing locally.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
# Declare where "collectstatic" shall place static files
# os.path.split(BASE_DIR)[0] is the parent directory of BASE_DIR
STATIC_ROOT = os.path.join(os.path.split(BASE_DIR)[0], 'numfys_static')

# The directory in which user-uploaded files are stored.
MEDIA_ROOT = os.path.join(os.path.split(BASE_DIR)[0], 'numfys_media')
MEDIA_URL = '/media/'
