from sentry.conf.server import *

import os.path

from decouple import config

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME', default='sentry'),
        'USER': config('DB_USER', default='sentry'),
        'PASSWORD': config('DB_USER', default='sentry'),
        'HOST': config('DB_HOST', default='db'),
        'PORT': config('DB_PORT', default=5432, cast=int)
    }
}

# You should not change this setting after your database has been created
# unless you have altered all schemas first
SENTRY_USE_BIG_INTS = True

# If you're expecting any kind of real traffic on Sentry, we highly recommend
# configuring the CACHES and Redis settings

###########
## Redis ##
###########

# Generic Redis configuration used as defaults for various things including:
# Buffers, Quotas, TSDB

SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': config('REDIS_HOST', default='redis'),
            'port': 6379,
        }
    }
}

###########
## Cache ##
###########

# If you wish to use memcached, install the dependencies and adjust the config
# as shown:
#
#   pip install python-memcached
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': ['127.0.0.1:11211'],
#     }
# }
#
# SENTRY_CACHE = 'sentry.cache.django.DjangoCache'

SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

###########
## Queue ##
###########

# See http://sentry.readthedocs.org/en/latest/queue/index.html for more
# information on configuring your queue broker and workers. Sentry relies
# on a Python framework called Celery to manage queues.

CELERY_ALWAYS_EAGER = False
BROKER_URL = config('redis://redis:6379', default='redis://localhost:6379')

#################
## Rate Limits ##
#################

SENTRY_RATELIMITER = 'sentry.ratelimits.redis.RedisRateLimiter'

####################
## Update Buffers ##
####################

# Buffers (combined with queueing) act as an intermediate layer between the
# database and the storage API. They will greatly improve efficiency on large
# numbers of the same events being sent to the API in a short amount of time.
# (read: if you send any kind of real data to Sentry, you should enable buffers)

SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'

############
## Quotas ##
############

# Quotas allow you to rate limit individual projects or the Sentry install as
# a whole.

SENTRY_QUOTAS = 'sentry.quotas.redis.RedisQuota'

##########
## TSDB ##
##########

# The TSDB is used for building charts as well as making things like per-rate
# alerts possible.

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'

################
## Web Server ##
################

# You MUST configure the absolute URI root for Sentry:
SENTRY_URL_PREFIX = config('SENTRY_URL')  # No trailing slash!

# If you're using a reverse proxy, you should enable the X-Forwarded-Proto
# and X-Forwarded-Host headers, and uncomment the following settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 8080
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'limit_request_line': 0,  # required for raven-js
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

#################
## Mail Server ##
#################

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)

# The email address to send on behalf of
SERVER_EMAIL = config('SERVER_EMAIL', default='sentry@localhost')

###########
## etc. ##
###########

# If this file ever becomes compromised, it's important to regenerate your SECRET_KEY
# Changing this value will result in all current sessions being invalidated
SECRET_KEY = 'YcrO63euA0PpvbUk/Yyd7FnOi3nK99HGdQb6Qh+RnaXRQyRArH8haQ==' # FIXME

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = config('TWITTER_CONSUMER_KEY', default='')
TWITTER_CONSUMER_SECRET = config('TWITTER_CONSUMER_SECRET', default='')

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = config('FACEBOOK_APP_ID', default='')
FACEBOOK_API_SECRET = config('FACEBOOK_API_SECRET', default='')

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = config('GOOGLE_OAUTH2_CLIENT_ID', default='')
GOOGLE_OAUTH2_CLIENT_SECRET = config('GOOGLE_OAUTH2_CLIENT_SECRET', default='')

# https://github.com/settings/applications/new
GITHUB_APP_ID = config('GITHUB_APP_ID', default='')
GITHUB_API_SECRET = config('GITHUB_API_SECRET', default='')

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = config('TRELLO_API_KEY', default='')
TRELLO_API_SECRET = config('TRELLO_API_SECRET', default='')

# https://confluence.atlassian.com/display/BITBUCKET/OAuth+Consumers
BITBUCKET_CONSUMER_KEY = config('BITBUCKET_CONSUMER_KEY', default='')
BITBUCKET_CONSUMER_SECRET = config('BITBUCKET_CONSUMER_SECRET', default='')
