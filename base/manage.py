#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Standard Library
import os
import sys


def main():
    """Run administrative tasks."""
    if not os.environ.get("DJANGO_SETTINGS_MODULE"):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
    else:
        print("Running in production, CAUTION!!!!")
        os.chdir(os.getcwd())
        print("Current Working Directory is: ", os.getcwd())
    try:
        # Django Libraries
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    # Normally, OAuthLib will raise an InsecureTransportError if you attempt to
    # use OAuth2 over HTTP, rather than HTTPS. Setting this environment variable
    # will prevent this error from being raised.
    # IMP: For non-docker based version.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    main()
