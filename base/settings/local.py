"""Django settings for local environment."""
# Local Vars
from .base import *  # noqa
from .base import env


# ------------------------------------------------------------------------------
# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY", default="!!!SET DJANGO_SECRET_KEY!!!")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "192.168.17.14"]
# https://github.com/adamchainz/django-cors-headers
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http:\/\/localhost:*([0-9]+)?$",
    r"^http:\/\/127.0.0.1:*([0-9]+)?$",
    r"^http:\/\/192.168.17.14:*([0-9]+)?$",
]

# ------------------------------------------------------------------------------
# DATABASES
# ------------------------------------------------------------------------------
# Parse database connection url strings
# https://django-environ.readthedocs.io/en/latest/types.html#term-PostgreSQL
DATABASES = {
    "default": env.db_url(
        "DATABASE_URL",
        default="postgres://root_user:some_random_password@db:5432/fitness_tracker_db",
    )
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------------------------------------------------
# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# ------------------------------------------------------------------------------
# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405


# ------------------------------------------------------------------------------
# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# #prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# #middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html
# #debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# #internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
# For docker development
if env("USE_DOCKER", default="N") == "Yes":
    # Standard Library
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
    try:
        _, _, ips = socket.gethostbyname_ex("node")
        INTERNAL_IPS.extend(ips)
    except socket.gaierror:
        # The node container isn't started (yet?)
        pass

# ------------------------------------------------------------------------------
# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest
# /installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405

# ------------------------------------------------------------------------------
# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in
# -development
# INSTALLED_APPS += ["whitenoise.runserver_nostatic"] #todo
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# ------------------------------------------------------------------------------
# django-webpack-loader
# ------------------------------------------------------------------------------
WEBPACK_LOADER["DEFAULT"]["CACHE"] = not DEBUG  # noqa F405

# ------------------------------------------------------------------------------
# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
# For non-docker based setup
# EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025
# IF not using `mailhog`:
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = env(
#     "DJANGO_EMAIL_BACKEND",
#     default="django.core.mail.backends.console.EmailBackend"
# )

# ------------------------------------------------------------------------------
# Security
# ------------------------------------------------------------------------------
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# ------------------------------------------------------------------------------
# Your stuff...
# ------------------------------------------------------------------------------
