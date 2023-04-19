"""URL mappings for the user API."""
# Django Libraries
from django.urls import path, re_path

# Project Libraries
from chat.views import all_rooms, room_detail, token


app_name = "chat"

urlpatterns = [
    path("", all_rooms, name="all_rooms"),
    path("token", token, name="token"),
    re_path(r"rooms/(?P<slug>[-\w]+)/$", room_detail, name="room_detail"),
]
