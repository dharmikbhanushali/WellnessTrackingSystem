"""All views related to sample api view. `api/sample`"""
# Standard Library
import logging

# Django Libraries
from django.conf import settings
from django.core.mail import mail_admins
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse

# 3rd Party Libraries
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.settings import api_settings

# Project Libraries
from prototype.serializer import PrototypeSerializer


logger = logging.getLogger("wrike_api")


class SampleMailAdmin(GenericAPIView):
    """Send sample email to admin using `mail_admins`."""

    permission_classes = [AllowAny]
    http_method_names = ["get"]
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = PrototypeSerializer

    def get(self, request, *args, **kwargs):
        template = get_template("wrike/mail_admins.html")
        user = "SOME RANDOM USER"
        subject = f"Grant access to WRIKE API for User: {user}"
        header = f"Hi {settings.ADMINS[0][0]},"
        message = f"""
                   The User: {user} has requested permission to access protected
                   resource:\
                   <b><code>{reverse("tasks:all_projects")}</code></b>.

                   Follow these steps to grant elevated access:
                   """
        end_note = f"""\
                   After granting access, the User: {user} will be treated as <b><code\
                   >staff</code></b> member and will have <b>READ_ONLY</b> \
                   access to protected resources.
                   """
        context = {
            "header": header,
            "message": message,
            "end_note": end_note,
            "user_id": 2,
        }
        content = template.render(context)
        mail_admins(subject, f"{header}\n{message}\n{end_note}", html_message=content)
        return Response({"Email sent...."})


class RenderSampleTemplate(GenericAPIView):
    """Render Sample template."""

    permission_classes = [AllowAny]
    http_method_names = ["get"]
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = PrototypeSerializer

    def get(self, request, *args, **kwargs):
        template = "wrike/mail_admins.html"
        user = "SOME RANDOM USER"
        header = f"Hi {settings.ADMINS[0][0]},"
        message = f"""
                       The User: {user} has requested permission to access protected
                       resource:\
                       <b><code>{reverse("tasks:all_projects")}</code></b>.

                       Follow these steps to grant elevated access:
                       """
        end_note = f"""\
                       After granting access, the User: {user} will be treated as
                       <b><code\
                       >staff</code></b> member and will have <b>READ_ONLY</b> \
                       access to protected resources.
                       """
        context = {
            "header": header,
            "message": message,
            "end_note": end_note,
            "user_id": 2,
        }

        return render(request, template, context)
