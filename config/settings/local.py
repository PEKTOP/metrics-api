from .base import *  # noqa

ALLOWED_HOSTS += ['127.0.0.1']  # noqa
INTERNAL_IPS = ALLOWED_HOSTS

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True
}

INSTALLED_APPS += [  # noqa
    'debug_toolbar',
]

MIDDLEWARE += [  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
