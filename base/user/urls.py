"""URL mappings for the user API."""
# Django Libraries
from django.urls import path

# Project Libraries
from user.views import UserDetailView, UserRedirectView, UserUpdateView


app_name = "user"

urlpatterns = [
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("~update/", view=UserUpdateView.as_view(), name="update"),
    path("<str:username>/", view=UserDetailView.as_view(), name="detail"),
]
