from conf.default import *

# All debugging activated
DEBUG = TEMPLATE_DEBUG = True

# Output emails to STDOUT
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/devops.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

# Use a folder outside of www for logs
LOGGING = create_logging_dict(location('/host/logs'))

# Don't use cached templates in development
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Use in-process cache by default
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Don't compress assets
COMPRESS_ENABLED = False

DEBUG_TOOLBAR_PATCH_SETTINGS = False

REGION = 'eu-west-1'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
KEY_NAME = 'devops-battlefield'
SECURITY_GROUPS = ['devops-battlefield-sg']
INSTANCE_TYPE = 't2.micro'
INSTANCE_PROFILE_NAME = 'ec2-s3'
AMI_ID = 'ami-fb5dcf8c'
