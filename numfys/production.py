"""
Production settings for running the NumFys Django app.
Imports base.py.
"""

from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's8+9!sa778c0b7m91sr_iz=p1mp1pnn&!mq459*=w=#n3%@)62'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['numfys.net', 'numfys.pythonanywhere.com', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
