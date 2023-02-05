"""
Serializers for the user API View. : `api/user`

Notes:
    W0223: Disable `Method is abstract in class but is not overridden(Pylint type
    checking)`.
"""
# pylint: disable = W0223
# Standard Library
import logging

# Django Libraries
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import mail_admins
from django.template.loader import get_template
from django.urls import reverse
from django.utils.translation import gettext as translate

# 3rd Party Libraries
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer, ValidationError

# Project Libraries
from settings.base import ADMINS


logger = logging.getLogger("wrike_api")


class UserSerializer(ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(Serializer):
    """Serializer for the user auth token."""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )
        if not user:
            msg_str = "Unable to authenticate with provided credentials."
            msg = translate(msg_str)
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class UpgradeUserSerializer(ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ["email", "name"]
        read_only_fields = ["email", "name"]

    def validate(self, attrs):
        """Validate the user is not already staff or admin user."""
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user.is_staff or user.is_superuser:
                err_msg = (
                    f"The user: {user.name} already has access to protected resources."
                )
                raise ValidationError(err_msg)
        return attrs

    def save(self, *args, **kwargs):
        """Prompt admin user to upgrade a normal user to staff user by sending email."""
        user = "Authenticated User"
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        user_name = user.name if hasattr(user, "name") else user
        template = get_template("wrike/mail_admins.html")
        subject = f"Grant access to WRIKE API for User: {user_name}"
        header = f"Hi {ADMINS[0][0]},"
        message = f"""
            The User: {user_name} has requested permission to \
            access protected resource: \
            <b><code>{reverse("tasks:all_projects")}</code></b>.

            Follow these steps to grant elevated access:
            """
        end_note = f"""\
            After granting access, the User: {user_name} will be treated as <b><code\
            >staff</code></b> member and will have <b>READ_ONLY</b> \
            access to protected resources.
            """
        context = {
            "header": header,
            "message": message,
            "end_note": end_note,
            "user_id": user.id if hasattr(user, "id") else 0,
        }
        content = template.render(context)
        mail_admins(
            subject,
            f"{header}\n{message}\n{end_note}",
            html_message=content,
        )


class DeleteUserSerializer(ModelSerializer):
    """Serializer for the deletion of user object."""

    email = serializers.EmailField(max_length=255)
    name = serializers.CharField(max_length=255)
