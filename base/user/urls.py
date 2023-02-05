"""URL mappings for the user API."""
# Django Libraries
from django.urls import path

# Project Libraries
from user.views import (
    CreateTokenView,
    CreateUserView,
    DeleteUserView,
    ManageUserView,
    UpgradeUserView,
)


app_name = "user"

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="me"),
    path("upgrade/", UpgradeUserView.as_view({"patch": "update"}), name="upgrade"),
    path("delete/<str:email>&<str:name>", DeleteUserView.as_view(), name="delete"),
]
