"""Views for the `api/user` API endpoint."""
# Standard Library
import logging

# Django Libraries
from django.contrib.auth import get_user_model

# 3rd Party Libraries
from rest_framework import authentication, generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet

# Project Libraries
from user.serializers import (
    AuthTokenSerializer,
    DeleteUserSerializer,
    UpgradeUserSerializer,
    UserSerializer,
)


logger = logging.getLogger("wrike_api")


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class UpgradeUserView(GenericViewSet, UpdateModelMixin):
    """Request access for protected resources.

    Notes:
        The admin user will assign certain `normal` users as `staff` users thus
        allowing access to protected resources using wrike `permanent token`.
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = UpgradeUserSerializer

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class DeleteUserView(generics.DestroyAPIView):
    """Allow superuser to delete staff user and normal users."""

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = DeleteUserSerializer
    lookup_fields = ("email", "name")

    def get_object(self):
        """Retrieve and return the normal user or staff user."""
        current_user = self.request.user
        if not current_user.is_superuser:
            raise PermissionDenied(
                f"Insufficient privileges. User:{current_user.name} is not admin user."
            )
        filter_kwargs = {
            lookup: self.kwargs.get(lookup) for lookup in self.lookup_fields
        }
        user = get_object_or_404(self.get_queryset(), **filter_kwargs)
        # May raise a permission denied
        self.check_object_permissions(self.request, user)
        if user.is_superuser:
            err_msg = f"The user: {user.name} is admin user. Please use admin portal."
            raise PermissionDenied(err_msg)
        return user
