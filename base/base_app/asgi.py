"""
ASGI config for base_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# Standard Library
import os

# Django Libraries
from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")

application = get_asgi_application()

# Import websocket application here, so apps from application are loaded first
from base_app.websocket import websocket_application  # noqa isort:skip


async def app(scope, receive, send):
    if scope["type"] == "http":
        await application(scope, receive, send)
    elif scope["type"] == "websocket":
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
