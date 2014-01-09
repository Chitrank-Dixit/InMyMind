"""
settings.py

Configuration for Flask app

Important: Place your keys in the secret_keys.py module, 
           which should be kept out of version control.

"""

import os

from secret_keys import CSRF_SECRET_KEY, SESSION_KEY


DEBUG_MODE = False

# Auto-set debug mode based on App Engine dev environ
if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    DEBUG_MODE = True

DEBUG = DEBUG_MODE

# Set secret keys for CSRF protection
SECRET_KEY = CSRF_SECRET_KEY
CSRF_SESSION_KEY = SESSION_KEY

CSRF_ENABLED = True

# Flask-DebugToolbar settings
DEBUG_TB_PROFILER_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False


# Flask-Cache settings
CACHE_TYPE = 'gaememcached'

# google settings file
GOOGLE_API_CLIENT_ID = '987638626090-2kanvsb99o2ij8j3vsvsebh7bul7tddr.apps.googleusercontent.com'
GOOGLE_API_CLIENT_SECRET = '4LkkuvOFHPCN2ziu58soAHQW'
GOOGLE_API_SCOPE = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'
GOOGLE_OAUTH2_URL = 'https://accounts.google.com/o/oauth2/'
GOOGLE_API_URL = 'https://www.googleapis.com/oauth2/v1/'


# recaptch made using Google 
# https://www.google.com/recaptcha/admin/site?siteid=317209387
RECAPTCHA_USE_SSL = True
RECAPTCHA_PUBLIC_KEY = '6Lccy-wSAAAAAHTPQJUvMpbqwhdwpN_M04Yg-UFp'
RECAPTCHA_PRIVATE_KEY = '6Lccy-wSAAAAAKCm7FnAQBelmguZqtG9zrN7V990'
# RECAPTCHA_OPTIONS = 

# flask-mail settings
# email server
MAIL_DEBUG = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'chitrankdixit1@gmail.com'
MAIL_PASSWORD = 'rossi46656915'
MAIL_SUPPRESS_SEND = False
